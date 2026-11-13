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
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            self.tasks.remove(task)
            # Reindex tasks
            for i, t in enumerate(self.tasks):
                t['id'] = i + 1
            print(f"✓ Task with ID {task_id} deleted")
        else:
            print(f"✗ Task with ID {task_id} not found")
    
    def mark_completed(self, task_id):
        """Mark task as completed"""
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            task['completed'] = True
            task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
            print(f"✓ Task with ID {task_id} marked as incomplete")
        else:
            print(f"✗ Task with ID {task_id} not found")


def main():
    """Main function"""
    print("Task Management Program")
    manager = TaskManager()


if __name__ == "__main__":
    main()
