FROM node:14-slim

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
