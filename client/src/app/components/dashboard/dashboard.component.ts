import { Component, OnInit } from "@angular/core";
import { TodoService } from "../../services/todo.service";

import { Todo } from "../../models/Todo";

@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.css"]
})
export class DashboardComponent implements OnInit {
  todos: Todo[];

  constructor(private todoService:TodoService) {}

  ngOnInit(): void {
    this.todoService.getTodos().subscribe(todos => this.todos = todos);
  }

  deleteTodo(todoToDelete:Todo) {
    this.todoService.deleteTodo(todoToDelete).subscribe(() => {
      this.todos = this.todos.filter(todo => todo.todoId !== todoToDelete.todoId);
    });
  }

  createTodo(data:Todo) {
    let body = {
      "title": data.title,
      "content": data.content,
      "completed": data.completed,
      "dueDate": data.dueDate,
      "priority": data.priority,
      "userId": data.user.userId
    };
    this.todoService.createTodo(body).subscribe(response => {
      data["todoId"] = response.todoId;
      this.todos.push(data);
    })
  }
}
