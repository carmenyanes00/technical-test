import './App.css';
import React, { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const [tasks, setTasks] = useState([]);
  const [newTaskName, setNewTaskName] = useState('');
  const url = "/tasks";

  useEffect(() => {
    fetch(url)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        const processedTasks = data.map(([id, name]) => ({ id, name }));
        setTasks(processedTasks);
      })
      .catch(error => console.error('Fetch error:', error));
  }, []);

  const handleAddTask = () => {
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: newTaskName }),
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        const newTask = { id: data.id, name: newTaskName };
        setTasks([...tasks, newTask]);
        setNewTaskName('');
      })
      .catch(error => console.error('Fetch error:', error));
  };

  return (
    <div className="App">
      <h1>Tasks</h1>
      <div>
        <input
          type="text"
          value={newTaskName}
          onChange={e => setNewTaskName(e.target.value)}
        />
        <button onClick={handleAddTask}>Add Task</button>
      </div>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;


