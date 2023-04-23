#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
    if (error) console.log(error);
    const todos = JSON.parse(body);
    const taskCount = {};

    for (let i = 0; i < todos.length; i++) {
	const todo = todos[i];
	if (todo.completed) {
            const userId = todo.userId;
	    if (!taskCount[userId]) {
		taskCount[userId] = 0;
	    }
	    taskCount[userId] = taskCount[userId] + 1;
      }
    };
    console.log(taskCount);
});
