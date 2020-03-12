import { Component, OnInit, Input, EventEmitter, Output } from "@angular/core";
import { Todo } from '../../models/Todo';

@Component({
  selector: "app-todo-card",
  templateUrl: "./todo-card.component.html",
  styleUrls: ["./todo-card.component.css"]
})
export class TodoCardComponent implements OnInit {
  @Input() todo: Todo;
  @Output() deleteTodo: EventEmitter<Todo> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  onDelete(todo) {
    this.deleteTodo.emit(todo);
  }
}
