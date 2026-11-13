#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Management Program
برنامه مدیریت وظایف
"""

import json
import os
from datetime import datetime


class TaskManager:
    """Main task manager class"""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            print("✓ Tasks saved successfully")
        except IOError:
            print("✗ Error saving tasks")
    
    def add_task(self, description):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added: {description}")
    
    def display_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks available")
            return

        print("\n" + "="*60)
        print("Task List:")
        print("="*60)
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
            print(f"    Created: {task['created_at']}")
            print("-"*60)
    
    def delete_task(self, task_id):
        """Delete a task"""
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            self.tasks.remove(task)
            # Reindex tasks
            for i, t in enumerate(self.tasks):
                t['id'] = i + 1
            self.save_tasks()
            print(f"✓ Task with ID {task_id} deleted")
        else:
            print(f"✗ Task with ID {task_id} not found")
    
    def mark_completed(self, task_id):
        """Mark task as completed"""
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            task['completed'] = True
            task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_tasks()
            print(f"✓ Task with ID {task_id} marked as completed")
        else:
            print(f"✗ Task with ID {task_id} not found")
    
    def mark_incomplete(self, task_id):
        """Mark task as incomplete"""
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            task['completed'] = False
            if 'completed_at' in task:
                del task['completed_at']
            self.save_tasks()
            print(f"✓ Task with ID {task_id} marked as incomplete")
        else:
            print(f"✗ Task with ID {task_id} not found")


def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("Task Management Program")
    print("="*60)
    print("1. Add new task")
    print("2. Display task list")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. Mark task as incomplete")
    print("6. Exit program")
    print("="*60)


def main():
    """Main function"""
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("\nPlease enter your choice (1-6): ")
        
        if choice == '1':
            description = input("Task description: ")
            if description.strip():
                manager.add_task(description)
            else:
                print("✗ Task description cannot be empty")
        
        elif choice == '2':
            manager.display_tasks()
        
        elif choice == '3':
            manager.display_tasks()
            try:
                task_id = int(input("\nEnter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("✗ Please enter a valid number")
        
        elif choice == '4':
            manager.display_tasks()
            try:
                task_id = int(input("\nEnter task ID to mark as completed: "))
                manager.mark_completed(task_id)
            except ValueError:
                print("✗ Please enter a valid number")
        
        elif choice == '5':
            manager.display_tasks()
            try:
                task_id = int(input("\nEnter task ID to mark as incomplete: "))
                manager.mark_incomplete(task_id)
            except ValueError:
                print("✗ Please enter a valid number")
        
        elif choice == '6':
            print("Exiting program...")
            break
        
        else:
            print("✗ Invalid option. Please try again")


if __name__ == "__main__":
    main()
