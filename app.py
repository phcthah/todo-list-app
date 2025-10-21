# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành"""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã đánh dấu hoàn thành: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ.")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách"""
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Đã xóa công việc: '{removed['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ.")

def list_tasks():
    """Liệt kê tất cả các công việc hiện có với trạng thái"""
    print("\nDanh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và Github")
    add_task("Làm bài tập thực hành ở nhà")
    complete_task(0)      # Đánh dấu công việc đầu tiên là hoàn thành
    delete_task(1)        # Xóa công việc thứ hai
    list_tasks()