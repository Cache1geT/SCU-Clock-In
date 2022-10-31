
# 免责声明
**坚定地清零，科学地打卡，本仓库只供交流学习**

打卡脚本修改自CarrotsPie/ZJU-nCov-Hitcarder的开源代码

README修改自Di-Zhipeng/ZJU-Clock-In

感谢两位同学开源的代码

如果这个仓库帮到了你，请给我一颗star 哈哈。

# 仓库功能

- 只需要一个github账号即可部署的自动打卡。

- 默认使用前一天的数据（所在位置，是否做了核酸等）打卡。

- 在每天的三个时间点随机打卡，以防打卡时间过于集中；并在每天快结束时补打一次，保证不会漏掉打卡。

# 配置教程

 **见仓库内的pdf文件**



# Q&A

## Q1: 这个脚本安全么？

这个脚本是开源的，大家可以自由观看它的代码，内容很简单。**没有任何窃取个人信息的操作**

我们的账户密码是放入github的secret中的，只有仓库的所有者才能看到你设置的ACCOUNT和PASSWORD。

这个项目的所有者虽然是我，但你是先Fork再操作的，此时Fork得到的仓库所有者是你自己，我们所有的操作都是在Fork后进行的，我是没有办法看到你的secret的。

所以**只要保证你自己的github账号密码不泄漏，你的密码就是安全的。**

## Q2: 我需要有专用的服务器或者设备来部署这个脚本吗？

**不需要**，本仓库使用github action执行定时任务。**只需要有一个github账号即可。**

github 对用户提供每月至少2000分钟的免费服务，用来运行我们的脚本绰绰有余。

另外建议使用常用邮箱注册github账号。因为当自动打卡程序执行失败时，github会给你发邮件提醒。
