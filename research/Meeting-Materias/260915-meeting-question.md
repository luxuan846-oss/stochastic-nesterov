
Q1: 老师，Bot给了三个idea，他对随机算法目前很感兴趣（而我做过stochastic optimization相关的），核心是搞清楚
Stochastic Nesterov momentum scheme，在凸光滑（无需强凸）问题上的收敛速度的分析框架、在什么条件下构造什么样的利亚普诺函数来分析O和o的收敛速度（加速与否？），和确定的相比，随机噪声会带来哪些影响。先和他讨论这篇：https://link.springer.com/article/10.1007/s10957-026-02940-4。
我感觉随机的假设和方差的控制会让分析的难度增加（构造势函数函数）。

我导师：
1. 这个似乎跟王老师的课题很相关。他给的是一个大方向，里面有好多问题已经解决了。剩下的问题得好好整理挑一个他关注的问题

2. 刚刚发的这篇文章注重讨论了加速参数对收敛速度的影响 2609.09152v2 2.pd； 目前在确定梯度法关于最优的步长，以及复杂度上下界的讨论热火朝天；不知道这两条线能不能碰撞出新的火花：

3. Bot让讨论的那篇，感觉苦劳比较大，看不出来啥功劳

我：
Q2: 老师，这个是为啥哇。我浏览了一遍，给我的感觉是把已有的确定加速的分析框架，扩展到了随机场景，恢复了确定的加速的-2的结果，但是恢复需要的条件都是充分条件；

这篇文章里的[28]，里面提到的是的asymptotic almost sure convergence rate应该是Bot关注的，他做的是极限收敛，不咋做复杂度。
Liu, J., Yuan, Y.: On almost sure convergence rates of stochastic gradient methods. In: The
35th Conference on Learning Theory (COLT), vol. 178, pp. 2963–2983. PMLR (2022).
https://proceedings.mlr.press/v178/liu22d.html

我导师：
1. 我个人觉得这两个都, 是苦劳：修补了28 41的证明小漏洞，推广了参数的取值范围。但是没有新的结论，比如在参数合适的选取条件下，理论或者数值会增强;
![[5511.png]]
2. https://proceedings.mlr.press/v178/liu22d.html 这篇文章确实不错，而且后续有JMLR长文
3. asymptotic almost sure convergence rate不错，如果能学会那很好。我问了一下大概要补的概率基础
4. 不知道这里的讨论，能不能推广到随机，研究symptotic almost sure convergence rate