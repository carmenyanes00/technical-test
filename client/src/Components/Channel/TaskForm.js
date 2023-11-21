import React, { useState } from 'react';

const TaskForm = () => {
  const [taskName, setTaskName] = useState('');

  const handleTaskSubmit = async () => {
    try {
      await fetch('http://localhost:5000/tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: taskName }),
      });

      window.location.reload();
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  return (
    <div>
      <h2>Create Task</h2>
      <input
        type="text"
        value={taskName}
        onChange={e => setTaskName(e.target.value)}
      />
      <button onClick={handleTaskSubmit}>Create</button>
    </div>
  );
};

export default TaskForm;
