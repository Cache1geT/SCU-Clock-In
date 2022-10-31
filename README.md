
# 声明
**坚定地清零，科学地打卡，本仓库仅供交流学习** : )

打卡脚本修改自CarrotsPie/ZJU-nCov-Hitcarder的开源代码

README修改自Di-Zhipeng/ZJU-Clock-In

感谢两位同学开源的代码

如果这个仓库帮到了你，请给我一颗star 哈哈。

# 仓库功能

- 只需要一个github账号即可实现自动打卡。

- 默认使用前一天的数据（所在位置，是否做了核酸等）打卡。

- 在每天的三个时间点随机打卡，以防打卡时间过于集中；并在每天快结束时补打一次，保证不会漏掉打卡。

# 自动打卡教程

 **若图片不可见，可查看仓库内的pdf文件**

打卡脚本修改自CarrotsPie/ZJU-nCov-Hitcarder的开源代码

README修改自Di-Zhipeng/ZJU-Clock-In

感谢两位同学开源的代码

如果这个仓库帮到了你，请给我一颗star 哈哈。

首先你需要拥有一个github账号，直接在左上角注册就行了。

### Step1. Fork本仓库

点击本仓库的Fork

![1](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/1.png?raw=true)

Fork的含义是将本仓库拷贝一份，放到你自己的github账号下，所以只有在第一次观看本教程的时候才需要fork。

然后我们可以看到，左上角这里的账户名已经变成了你自己账号的名字。

![2](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/2.png?raw=true)

此时你已经拥有了本仓库的一个拷贝。

### Step2. 添加账户密码

点击仓库的右上角的Settings：

![3](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/3.png?raw=true)

点击下面的Secret

![4](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/4.png?raw=true)

点击右上角的New repository Secret，添加一个Secret

![5](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/5.png?raw=true)

Name必须为ACCOUNT，Secret填入自己的川大微服务认证系统的账号，注意Name和Value的值前后不要有多余空格。

![7](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/7.png?raw=true)

然后仿照上面的操作再添加一个。Name设为PASSWORD，Secret填入川大微服务认证系统的密码，自动打卡脚本就配置完成了。

![8](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/8.png?raw=true)

效果和下面的差不多：

![9](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/9.png?raw=true)

开启github action：

![10](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/10.png?raw=true)

### Step3. 如何触发打卡？

有两种方式，第一种是在自己的SCU-Clock-In仓库里点击Star（已经Star的就取消Star，再重新点击）。

第二种是等待，这个脚本在每天的三个时间点触发,代码里做了简单的随机，防止打卡时间过于集中在一个时间段。

### Step4. 如何判断打卡是否成功？

点击仓库的Action：

![11](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/11.png?raw=true)

每次触发打卡就会在右边多出一个记录，比如现在我已经执行过三次打卡脚本了，点击你需要查看的记录，再点击里面的ClockIn按钮，我们就可以看到本次打卡的情况了：

![12](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/12.png?raw=true)

非计算机科学的学生只需要关注右侧ClockIn的文字提示内容就行了，点击Clock In：

![13](https://github.com/Cache1geT/SCU-Clock-In/blob/master/imgs/13.png?raw=true)

就可以看到提示信息了，如果打卡失败，就按照提示去操作就好了。

## Q&A

### Q1: 这个脚本安全吗？

这个脚本是开源的，大家可以自由观看它的代码，内容很简单，没有任何窃取个人信息的操作

我们的账户密码是放入github的secret中的，只有仓库的所有者才能看到你设置的ACCOUNT和PASSWORD。

这个项目的所有者虽然是我，但你是先Fork再操作的，此时Fork得到的仓库所有者是你自己，我们所有的操作都是在Fork后进行的，我是没有办法看到你的secret的。

所以只要保证你自己的github账号密码不泄漏，你的密码就是安全的。

### Q2: 我需要有专用的服务器或者设备来部署这个脚本吗？

不需要，本仓库使用github action执行定时任务。只需要有一个github账号即可。

github 对用户提供每月至少2000分钟的免费服务，用来运行我们的脚本绰绰有余。

另外建议使用常用邮箱注册github账号。因为当自动打卡程序执行失败时，github会给你发邮件提醒。
