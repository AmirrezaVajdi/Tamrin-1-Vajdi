#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Management Program
برنامه مدیریت وظایف
"""

from datetime import datetime


class TaskManager:
    """Main task manager class"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
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
        pass
    
    def mark_completed(self, task_id):
        """Mark task as completed"""
        pass


def main():
    """Main function"""
    print("Task Management Program")
    manager = TaskManager()


if __name__ == "__main__":
    main()
