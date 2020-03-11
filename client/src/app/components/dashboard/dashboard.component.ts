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
}
