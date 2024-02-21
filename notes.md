

## 一、起步

> 图书在线资料： https://www.ituring.com.cn/book/3038
>
> [python.org](https://www.python.org/)



### 使用Sublime Text

文件扩展名.py告诉Sublime Text，文件中的代码是使用Python编写的，这能让它知道如何运行这个程序，并以有帮助的方式突出其中的代码。

选择菜单**Tools  ——》 Build** 或按 **Ctrl + B**（在macOS系统中为Command + B）来运行程序。

![image-20240219234444768](C:\Users\kanji\AppData\Roaming\Typora\typora-user-images\image-20240219234444768.png)





### 使用VS Code

internalConsole  内部控制台

integratedTerminal  集成终端

![image-20240219232452512](C:\Users\kanji\AppData\Roaming\Typora\typora-user-images\image-20240219232452512.png)

让 VS Code 在调试控制台（而不是集成的终端窗口）中显示输出后，
将无法运行使用了 input()函数的程序。 调试控制台是只读的，这意味着它不能接受输入。  



![image-20240219234359549](C:\Users\kanji\AppData\Roaming\Typora\typora-user-images\image-20240219234359549.png)

从编辑器切换到终端窗口，可按 Ctrl + `；
提供程序输入后，可再次按 Ctrl +``从终端窗口切换到编辑器窗口  



## 二、变量和简单数据类型



### 2.2 变量

#### 变量的命名和使用：

* 变量名只能包含字母、数字和下划线。

* 能以字母或下划线打头，但不能以数字打头

* 变量名不能包含空格，能使用下划线来分隔其中的单词

* 不要将Python关键字和函数名用作变量名

* 应既简短又具有描述性

* 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

* 目前而言，应使用小写的Python变量名。

  虽然在变量名中使用大写字母不会导致错误，但是大写字母在变量名中有特殊含义



#### traceback

程序无法成功运行时，解释器将提供一个traceback。

traceback是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。







## 附录D 使用Git进行版本控制

### 配置 .gitignore

```
pycache  // 忽略pycache文件夹
resources  // 忽略resources文件夹
```



### 撤销修改

放弃最后一次提交后所做的所有修改，将项目恢复到最后一次提交的状态

```
git checkout .
```











