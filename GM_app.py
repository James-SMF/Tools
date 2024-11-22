import tkinter as tk
from tkinter import ttk, messagebox

# 创建GM指令的封装类
class GMCommandApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GM Command Builder")

        # 指令列表
        self.command_list = []

        # 创建UI
        self.create_ui()

    def create_ui(self):
        # 输入框
        self.command_frame = ttk.LabelFrame(self.root, text="添加 GM 指令")
        self.command_frame.grid(row=0, column=0, padx=10, pady=10)

        # 指令类型选择
        ttk.Label(self.command_frame, text="指令类型:").grid(row=0, column=0, sticky="w")
        self.command_type = ttk.Combobox(
            self.command_frame, values=["kick", "ban", "warn", "give", "heal", "teleport"], state="readonly"
        )
        self.command_type.grid(row=0, column=1, padx=5, pady=5)
        self.command_type.set("kick")

        # 参数输入
        ttk.Label(self.command_frame, text="玩家名/参数:").grid(row=1, column=0, sticky="w")
        self.param_entry = ttk.Entry(self.command_frame)
        self.param_entry.grid(row=1, column=1, padx=5, pady=5)

        # 添加指令按钮
        add_button = ttk.Button(self.command_frame, text="添加指令", command=self.add_command)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # 显示命令队列
        self.queue_frame = ttk.LabelFrame(self.root, text="指令队列")
        self.queue_frame.grid(row=1, column=0, padx=10, pady=10)

        self.command_listbox = tk.Listbox(self.queue_frame, height=10, width=50)
        self.command_listbox.grid(row=0, column=0, padx=5, pady=5)

        # 操作按钮
        self.action_frame = ttk.Frame(self.root)
        self.action_frame.grid(row=2, column=0, pady=10)

        run_button = ttk.Button(self.action_frame, text="运行指令", command=self.run_commands)
        run_button.grid(row=0, column=0, padx=10)

        clear_button = ttk.Button(self.action_frame, text="清空队列", command=self.clear_commands)
        clear_button.grid(row=0, column=1, padx=10)

    def add_command(self):
        """将指令添加到队列中"""
        command_type = self.command_type.get()
        param = self.param_entry.get()

        if not param:
            messagebox.showerror("错误", "参数不能为空！")
            return

        command = f"/{command_type} {param}"
        self.command_list.append(command)
        self.update_listbox()
        self.param_entry.delete(0, tk.END)

    def update_listbox(self):
        """刷新命令队列显示"""
        self.command_listbox.delete(0, tk.END)
        for command in self.command_list:
            self.command_listbox.insert(tk.END, command)

    def run_commands(self):
        """模拟运行所有命令"""
        if not self.command_list:
            messagebox.showinfo("提示", "当前没有指令可运行。")
            return

        # 模拟执行（这里你可以改成调用实际的GM接口）
        for command in self.command_list:
            print(f"执行指令: {command}")

        messagebox.showinfo("运行完成", "所有指令已执行！")

    def clear_commands(self):
        """清空命令队列"""
        self.command_list.clear()
        self.update_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    app = GMCommandApp(root)
    root.mainloop()

