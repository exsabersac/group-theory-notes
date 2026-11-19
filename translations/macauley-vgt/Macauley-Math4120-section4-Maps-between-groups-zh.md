# 第 4 节：群之间的映射

原名：*Section 4: Maps between groups*

原作者：Matthew Macauley（Clemson University, Department of Mathematical Sciences）

课程：Math 4120 Modern Algebra（2020 年夏季课程材料；配套 Visual Group Theory 视频课）

许可：本译本为原讲义的演绎作品，与原文同以 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 发布。这是*非官方中译本*，仅供学习对照，并非官方中文版。

原课程页：<https://www.math.clemson.edu/~macaule/classes/m20_math4120/>  
许可说明索引：<https://www.math.clemson.edu/~macaule/youtube.html>

说明：公式使用 `$...$`（Typst / 类 TeX 记号）。完整对照版（含原幻灯片图像）见同目录下的 PDF。

## 第 1 页 / 51

**第 4 节：群之间的映射**

Matthew Macauley

克莱姆森大学数学科学系
Clemson University
http://www.math.clemson.edu/~macaule/

Math 4120，近世代数（Modern Algebra）

## 第 2 页 / 51

**同态**

在整个课程中，我们曾说过这样的话：

- “这个群与那个群具有相同的结构。”
- “这个群同构于那个群。”

不过，我们从未真正把“这究竟意味着什么”的细节说清楚。

我们将研究群之间一种特殊类型的函数，称为 *同态*。*同构* 是一种特殊的同态。希腊语词根 “homo” 与 “morph” 合在一起的意思是“相同的形状”。

同态出现在两种情形中：

- 当一个群是另一个群的子群时；
- 当一个群是另一个群的商时。

相应的同态分别称为 *嵌入* 与 *商映射*。

同样在这一章中，我们将完全分类所有有限阿贝尔群，并初步接触若干更高级的课题，例如四个“同构定理”、换位子群，以及自同构。

## 第 3 页 / 51

**一个启发性的例子**

考虑断言：$ZZ_3 < D_3$。下面是一种视觉表示（见原图）：$0 |-> e$，$1 |-> r$，$2 |-> r^2$。

群 $D_3$ 含有一个 3 阶循环子群 $angle.l r angle.r$，它只是在结构上与 $ZZ_3$ 相同。$ZZ_3$ 的元素（即 $0, 1, 2$）实际上并不在 $D_3$ 中。

当我们说 $ZZ_3 < D_3$ 时，真正的意思是：$ZZ_3$ 的结构出现在 $D_3$ 中。

特别地，$ZZ_3$ 中的元素与 $D_3$ 中子群 $angle.l r angle.r$ 的元素之间存在双射对应。而且，相对应的节点之间的关系是相同的。

同态是用来简洁而精确地表达结构对应的数学工具。它是满足若干“自然”性质的、群之间的函数。

## 第 4 页 / 51

**同态**

沿用前面的例子，我们说这个函数把 $ZZ_3$ 的元素映到 $D_3$ 的元素，由 $phi(n) = r^n$ 给出。我们可以把它写成

$phi : ZZ_3 -> D_3$。

函数出发的那个群称为 *定义域*（在我们的例子中是 $ZZ_3$）。函数所映入的那个群称为 *陪域*（在我们的例子中是 $D_3$）。

函数所映到的那些陪域中的元素，称为该函数的 *像*（在我们的例子中是 ${e, r, r^2}$），记作 $"Im"(phi)$。也就是说，

$"Im"(phi) = phi(G) = {phi(g) mid(|) g in G}$。

**定义**
同态是两个群之间的函数 $phi : G -> H$，满足

$phi(a b) = phi(a) phi(b)$，对所有 $a, b in G$。

注意，运算 $a dot b$ 发生在定义域中，而 $phi(a) dot phi(b)$ 发生在陪域中。

## 第 5 页 / 51

**同态**

**注记**
并非从一个群到另一个群的每一个函数都是同态！条件 $phi(a b) = phi(a) phi(b)$ 意味着映射 $phi$ 保持 $G$ 的结构。

条件 $phi(a b) = phi(a) phi(b)$ 在凯莱图与乘法表的层面上有视觉解释（见原图）。

注意，在凯莱图中，$b$ 与 $phi(b)$ 是路径；它们不必只是边。

## 第 6 页 / 51

**一个例子**

考虑把一个整数模 5 约化的函数：

$phi : ZZ -> ZZ_5$，$phi(n) = n$ （模 5）。

由于群运算是加法的， “同态性质”变成

$phi(a + b) = phi(a) + phi(b)$。

用白话说，这不过是在说：人们可以“先相加再模 5 约化”，也可以“先模 5 约化再相加”。

（见原图中定义域 $ZZ$ 与陪域 $ZZ_5$ 的凯莱图片段及加法表示意。）

## 第 7 页 / 51

**同态的类型**

考虑下面的同态 $theta : ZZ_3 -> C_6$，由 $theta(n) = r^(2 n)$ 定义（见原图）：$0 |-> 1$，$1 |-> r^2$，$2 |-> r^4$。

容易验证 $theta(a + b) = theta(a) theta(b)$：$ZZ_3$ 中表示 1 的红色箭头，被映到 $C_6$ 中表示 $r^2$ 的两步路径。

一对一或“单射”的同态 $phi : G -> H$ 称为 *嵌入*：群 $G$ “嵌入” $H$ 成为一个子群。若 $theta$ 不是一对一的，则它是一个 *商*。

若 $phi(G) = H$，则 $phi$ 是到上的，或 *满射的*。

**定义**
既是单射又是满射的同态称为 *同构*。
*自同构* 是从一个群到它自身的同构。

## 第 8 页 / 51

**同态与生成元**

**注记**
若我们知道一个同态把 $G$ 的生成元映到何处，就可以确定它把 $G$ 的所有元素映到何处。

例如，假设 $phi : ZZ_3 -> ZZ_6$ 是一个同态，且 $phi(1) = 4$。利用这一信息，我们可以构造出 $phi$ 的其余部分：

$phi(2) = phi(1 + 1) = phi(1) + phi(1) = 4 + 4 = 2$

$phi(0) = phi(1 + 2) = phi(1) + phi(2) = 4 + 2 = 0$。

**例子**
假设 $G = angle.l a, b angle.r$，且 $phi : G -> H$，并且我们知道 $phi(a)$ 与 $phi(b)$。利用这些信息，我们可以确定 $G$ 中任意元素的像。例如，对 $g = a^3 b^2 a b$，我们有

$phi(g) = phi(a a a b b a b) = phi(a) phi(a) phi(a) phi(b) phi(b) phi(a) phi(b)$。

你认为 $phi(a^(-1))$ 是什么？

## 第 9 页 / 51

**同态的两条基本性质**

**命题**
设 $phi : G -> H$ 是一个同态。把 $G$ 的单位元记作 $1_G$，把 $H$ 的单位元记作 $1_H$。

1. $phi(1_G) = 1_H$ “$phi$ 把单位元送到单位元”
2. $phi(g^(-1)) = phi(g)^(-1)$ “$phi$ 把逆元送到逆元”

**证明**
1. 任取 $g in G$。现在 $phi(g) in H$；观察

$phi(1_G) phi(g) = phi(1_G dot g) = phi(g) = 1_H dot phi(g)$。

因此 $phi(1_G) = 1_H$。

2. 任取 $g in G$。观察

$phi(g) phi(g^(-1)) = phi(g g^(-1)) = phi(1_G) = 1_H$。

由于 $phi(g) phi(g^(-1)) = 1_H$，立即得到 $phi(g^(-1)) = phi(g)^(-1)$。证毕。

## 第 10 页 / 51

**一句警告**

同态 $phi : G -> H$ 由生成元的像所确定，这并不意味着任意指定这样的像都行得通。

例如，假设我们试图用 $phi(1) = 1$ 来定义一个同态 $phi : ZZ_3 -> ZZ_4$。则我们得到

$phi(2) = phi(1 + 1) = phi(1) + phi(1) = 2$，

$phi(0) = phi(1 + 1 + 1) = phi(1) + phi(1) + phi(1) = 3$。

这是不可能的，因为必须有 $phi(0) = 0$。（单位元被映到单位元。）

这并不是说不存在同态 $phi : ZZ_3 -> ZZ_4$；注意，两个群之间总存在 *平凡同态*：

$phi : G -> H$，$phi(g) = 1_H$ 对所有 $g in G$。

**练习**
证明：对 $n >= 2$，不存在嵌入 $phi : ZZ_n arrow.r.hook ZZ$。也就是说，任何这样的同态都必须满足 $phi(1) = 0$。

## 第 11 页 / 51

**同构**

两个同构的群可能给它们的元素起不同的名字，并且由于凯莱图的布局或生成元选择不同，看起来也可能不同，但它们之间的同构保证它们具有相同的结构。

当两个群 $G$ 与 $H$ 之间存在同构时，我们说 $G$ 与 $H$ *同构*，并写成 $G tilde.eq H$。

多项式 $f(x) = x^4 - 1$ 的根称为 4 次单位根，记作 $R(4) := {1, i, -1, -i}$。它们是 $CC^* := CC without {0}$（非零复数乘法群）的一个子群。

下面的映射是 $ZZ_4$ 与 $R(4)$ 之间的一个同构：

$phi : ZZ_4 -> R(4)$，$phi(k) = i^k$。（见原图）

## 第 12 页 / 51

**同构**

有时，由于凯莱图具有不同的结构，同构在视觉上并不那么明显。

例如，下面是一个同构：$phi : ZZ_6 -> C_6$，$phi(k) = r^k$。（见原图）

这里还有一个不那么明显的同构，介于 $S_3 = angle.l (1 2), (2 3) angle.r$ 与 $D_3 = angle.l r, f angle.r$ 之间：

$phi : S_3 -> D_3$，$phi : (1 2) |-> r f$，$phi : (2 3) |-> f$。（见原图）

## 第 13 页 / 51

**另一个例子：四元数**

令 $"GL"_n (RR)$ 为以实数为条目的可逆 $n times n$ 矩阵的集合。容易看出，它在乘法下构成一个群。

回想四元数群 $Q_8 = angle.l i, j, k mid(|) i^2 = j^2 = k^2 = -1, i j = k angle.r$。

下面这组 8 个矩阵在乘法下构成一个同构的群，其中 $I$ 是 $4 times 4$ 单位矩阵。（具体矩阵见原图。）

形式上，我们有一个嵌入 $phi : Q_8 -> "GL"_4 (RR)$，其中 $phi(i)$、$phi(j)$、$phi(k)$ 为原图所示的那些矩阵。

我们说 $Q_8$ 由一组矩阵所 *表示*。

许多其他群也可以用矩阵来表示。你能想出如何用矩阵来表示 $V_4$、$C_n$ 或 $S_n$ 吗？

## 第 14 页 / 51

**商映射**

考虑这样的同态：定义域中不止一个元素被映到陪域中的同一个元素（即非嵌入）。

这里有一些例子：$tau_1 : Q_8 -> V_4$，以及 $tau_2 : ZZ_10 -> ZZ_6$。（见原图）

非嵌入的同态称为 *商映射*（正如我们将看到的，它们对应于我们的商手续）。

## 第 15 页 / 51

**原像**

**定义**
若 $phi : G -> H$ 是一个同态且 $h in "Im"(phi) < H$，定义 $h$ 的 *原像* 为集合

$phi^(-1)(h) := {g in G : phi(g) = h}$。

观察前面的例子：所有原像都具有相同的结构。这件事总是成立的。（见原图示意图）

$1_H in H$ 的原像称为 $phi$ 的 *核*，记作 $"Ker" phi$。

## 第 16 页 / 51

**原像**

**观察 1**
$phi$ 的所有原像都具有相同的结构。

**证明（梗概）**
任取 $a, b in phi(G)$，并令 $A = phi^(-1)(a)$、$B = phi^(-1)(b)$ 为它们的原像。

考虑 $A$ 中元素之间的任意一条路径 $a_1 -> a_2$（沿着某条路径 $p$）。对任意 $b_1 in B$，都有一条相应的路径 $b_1 -> b_2$。我们需要证明 $b_2 in B$。

由于同态保持结构，$phi(a_1)$ 沿着 $phi(p)$ 到达 $phi(a_2)$。由于 $phi(a_1) = phi(a_2)$，$phi(p)$ 是平凡路径。

因此，$phi(b_1)$ 沿着 $phi(p)$ 到达 $phi(b_2)$，即 $phi(b_1) = phi(b_2)$，从而由定义有 $b_2 in B$。证毕。

显然，$G$ 被 $phi$ 的原像所划分。此外，我们刚刚证明它们都具有相同的结构。（听起来熟悉吗？）

## 第 17 页 / 51

**原像与核**

**定义**
同态 $phi : G -> H$ 的 *核* 是集合

$"Ker"(phi) := phi^(-1)(e) = {k in G : phi(k) = e}$。

**观察 2**
1. 单位元的原像（即 $K = "Ker"(phi)$）是 $G$ 的一个子群。
2. 所有其他原像都是 $K$ 的左陪集。

**证明（第 (i) 条）**
令 $K = "Ker"(phi)$，并取 $a, b in K$。我们必须证明 $K$ 满足 3 条性质：
*单位元：* $phi(e) = e$。
*封闭性：* $phi(a b) = phi(a) phi(b) = e dot e = e$。
*逆元：* $phi(a^(-1)) = phi(a)^(-1) = e^(-1) = e$。
因此，$K$ 是 $G$ 的一个子群。证毕。

## 第 18 页 / 51

**核**

**观察 3**
$"Ker"(phi)$ 是 $G$ 的一个正规子群。

**证明**
令 $K = "Ker"(phi)$。我们将证明：若 $k in K$，则 $g k g^(-1) in K$。任取 $g in G$，并观察

$phi(g k g^(-1)) = phi(g) phi(k) phi(g^(-1)) = phi(g) dot e dot phi(g^(-1)) = phi(g) phi(g)^(-1) = e$。

因此 $g k g^(-1) in "Ker"(phi)$，故 $K lt.tri.eq G$。证毕。

**关键观察**
给定任意同态 $phi : G -> H$，我们总可以形成商群 $G \/ "Ker"(phi)$。

## 第 19 页 / 51

**商：通过乘法表**

回想 $C_2 = {e^(0 pi i), e^(1 pi i)} = {1, -1}$。考虑下面的（商）同态：

$phi : D_4 -> C_2$，由 $phi(r) = 1$ 与 $phi(f) = -1$ 定义。

注意 $phi("旋转") = 1$ 且 $phi("反射") = -1$。

把 $D_4$ “缩小成 $C_2$” 的商手续，可以从乘法表中清楚地看出：表按非翻转／翻转分成块，商后得到 $C_2$ 的乘法表（见原图）。

## 第 20 页 / 51

**商：通过凯莱图**

定义同态 $phi : Q_8 -> V_4$，由 $phi(i) = v$ 与 $phi(j) = h$ 给出。由于 $Q_8 = angle.l i, j angle.r$，我们可以确定 $phi$ 把其余元素送到何处：

$phi(1) = e$，$phi(-1) = phi(i^2) = phi(i)^2 = v^2 = e$，

$phi(k) = phi(i j) = phi(i) phi(j) = v h = r$，$phi(-k) = phi(j i) = phi(j) phi(i) = h v = r$，

$phi(-i) = phi(-1) phi(i) = e v = v$，$phi(-j) = phi(-1) phi(j) = e h = h$。

注意 $"Ker" phi = {-1, 1}$。让我们看看用 $"Ker" phi$ 去除时会发生什么（见原图）：按子群 $K = angle.l -1 angle.r$ 组织 $Q_8$，左陪集彼此靠近，再把陪集坍缩成单个节点，得到 $Q_8 \/ K$。

你是否注意到 $Q_8 \/ "Ker"(phi)$ 与 $"Im"(phi)$ 之间有什么关系？

## 第 21 页 / 51

**基本同态定理**

下面是群论中的中心结果之一。

**基本同态定理（FHT）**
若 $phi : G -> H$ 是一个同态，则 $"Im"(phi) tilde.eq G \/ "Ker"(phi)$。

FHT 说：每一个同态都可以分解成两步：(i) 用核去除，然后 (ii) 通过 $phi$ 给节点重新标记。

（见原图：从 $G$ 出发的任意同态 $phi$ 到达 $"Im" phi$；先经商手续 $q$ 得到陪集的群 $G \/ "Ker" phi$，再经剩余的同构 $i$（“重新标记”）到达 $"Im" phi$。）

## 第 22 页 / 51

**FHT 的证明**

**基本同态定理**
若 $phi : G -> H$ 是一个同态，则 $"Im"(phi) tilde.eq G \/ "Ker"(phi)$。

**证明**
我们将构造一个显式的映射 $i : G \/ "Ker"(phi) -> "Im"(phi)$，并证明它是一个同构。
令 $K = "Ker"(phi)$，并回想 $G \/ K = {a K : a in G}$。定义

$i : G \/ K -> "Im"(phi)$，$i : g K |-> phi(g)$。

- 证明 $i$ 是良好定义的：我们必须证明，若 $a K = b K$，则 $i(a K) = i(b K)$。
假设 $a K = b K$。我们有

$a K = b K arrow.r.double b^(-1) a K = K arrow.r.double b^(-1) a in K$。

由 $b^(-1) a in "Ker"(phi)$ 的定义，

$1_H = phi(b^(-1) a) = phi(b^(-1)) phi(a) = phi(b)^(-1) phi(a)$，从而 $phi(a) = phi(b)$。

由 $i$ 的定义：$i(a K) = phi(a) = phi(b) = i(b K)$。

## 第 23 页 / 51

**FHT 的证明（续）**

［回想：$i : G \/ K -> "Im"(phi)$，$i : g K |-> phi(g)$］

**证明（续）**
- 证明 $i$ 是同态：我们必须证明 $i(a K dot b K) = i(a K) i(b K)$。

$i(a K dot b K) = i(a b K)$（因为 $a K dot b K := a b K$）

$= phi(a b)$（$i$ 的定义）

$= phi(a) phi(b)$（$phi$ 是同态）

$= i(a K) i(b K)$（$i$ 的定义）

因此，$i$ 是一个同态。

- 证明 $i$ 是满射（到上）：
这意味着：对陪域（这里是 $"Im"(phi)$）中的任意元素，定义域（这里是 $G \/ K$）中都有某个元素被 $i$ 映到它。

任取 $phi(a) in "Im"(phi)$。由定义，$i(a K) = phi(a)$，因此 $i$ 是满射。

## 第 24 页 / 51

**FHT 的证明（续）**

［回想：$i : G \/ K -> "Im"(phi)$，$i : g K |-> phi(g)$］

**证明（续）**
- 证明 $i$ 是单射（一对一）：我们必须证明 $i(a K) = i(b K)$ 蕴涵 $a K = b K$。

假设 $i(a K) = i(b K)$。则

$i(a K) = i(b K) arrow.r.double phi(a) = phi(b)$（由定义）

$arrow.r.double phi(b)^(-1) phi(a) = 1_H$

$arrow.r.double phi(b^(-1) a) = 1_H$（$phi$ 是同态）

$arrow.r.double b^(-1) a in K$（$"Ker"(phi)$ 的定义）

$arrow.r.double b^(-1) a K = K$（$a H = H arrow.l.r.double a in H$）

$arrow.r.double a K = b K$

因此，$i$ 是单射。

总之，由于 $i : G \/ K -> "Im"(phi)$ 是一个良好定义的、单射且满射的同态，它是一个同构。

因此 $G \/ K tilde.eq "Im"(phi)$，FHT 得证。证毕。

## 第 25 页 / 51

**FHT 的推论**

**推论**
若 $phi : G -> H$ 是一个同态，则 $"Im" phi <= H$。

**若干特殊情形**
- 若 $phi : G -> H$ 是嵌入，则 $"Ker"(phi) = {1_G}$。FHT 说：$"Im"(phi) tilde.eq G \/ {1_G} tilde.eq G$。
- 若 $phi : G -> H$ 是对所有 $g in G$ 都有 $phi(g) = 1_H$ 的映射，则 $"Ker"(phi) = G$，因此 FHT 说：${1_H} = "Im"(phi) tilde.eq G \/ G$。

让我们用 FHT 来确定所有同态 $phi : C_4 -> C_3$：

- 由 FHT，$G \/ "Ker" phi tilde.eq "Im" phi < C_3$，因此 $|"Im" phi| = 1$ 或 $3$。
- 由于 $"Ker" phi < C_4$，拉格朗日定理也告诉我们 $|"Ker" phi| in {1, 2, 4}$，从而 $|"Im" phi| = |G \/ "Ker" phi| in {1, 2, 4}$。

因此 $|"Im" phi| = 1$，所以唯一的同态 $phi : C_4 -> C_3$ 是平凡同态。

## 第 26 页 / 51

**“良好定义”究竟是什么意思？**

回想我们曾在不同语境中见到过“良好定义”这一用语：

- 陪集集合 $G \/ N$ 上的一个良好定义的二元运算，
- 从陪集的集合（群）出发的一个良好定义的函数 $i : G \/ N -> H$。

在这两种情形中，良好定义都意味着：

我们的定义不依赖于对陪集代表元的选择。

形式上：

- 若 $N lt.tri.eq G$，则 $a N dot b N := a b N$ 是陪集集合 $G \/ N$ 上一个良好定义的二元运算，因为：若 $a_1 N = a_2 N$ 且 $b_1 N = b_2 N$，则 $a_1 b_1 N = a_2 b_2 N$。
- 映射 $i : G \/ K -> H$，其中 $i(a K) = phi(a)$，是一个良好定义的同态，意味着：若 $a K = b K$，则 $i(a K) = i(b K)$（也就是 $phi(a) = phi(b)$）成立。

每当我们定义一个映射、并且定义域是一个商时，都必须证明它是良好定义的。

## 第 27 页 / 51

**如何证明两个群同构**

证明 $G tilde.eq H$ 的标准方法是构造一个同构 $phi : G -> H$。

当定义域是一个商时，由于 FHT，还有另一种方法。

**有用的技巧**
假设我们想证明 $G \/ N tilde.eq H$。有两种途径：

1. 定义一个映射 $phi : G \/ N -> H$，并证明它是良好定义的、是同态、并且是双射。
2. 定义一个映射 $phi : G -> H$，并证明它是同态、是满射（到上）、并且 $"Ker" phi = N$。

通常，方法 (ii) 更容易。证明良好定义性与单射性可能比较棘手。

例如，下面每条都是我们很快就会见到的结果，而方法 (ii) 对它们相当好用：

- $ZZ \/ angle.l n angle.r tilde.eq ZZ_n$；
- $QQ^* \/ angle.l -1 angle.r tilde.eq QQ^+$；
- $A B \/ B tilde.eq A \/ (A inter B)$（假定 $A, B lt.tri.eq G$）；
- $G \/ (A inter B) tilde.eq (G \/ A) times (G \/ B)$（假定 $G = A B$）。

## 第 28 页 / 51

**作为商的循环群**

考虑 $ZZ$ 的下列正规子群：

$12 ZZ = angle.l 12 angle.r = {dots, -24, -12, 0, 12, 24, dots} lt.tri.eq ZZ$。

商群 $ZZ \/ angle.l 12 angle.r$ 的元素是陪集：

$0 + angle.l 12 angle.r$，$1 + angle.l 12 angle.r$，$2 + angle.l 12 angle.r$，$dots$，$10 + angle.l 12 angle.r$，$11 + angle.l 12 angle.r$。

数论家把这些集合叫做模 12 的 *同余类*。我们说两个数模 12 同余，如果它们在同一个陪集中。

回想如何在商群中把陪集相加：

$(a + angle.l 12 angle.r) + (b + angle.l 12 angle.r) := (a + b) + angle.l 12 angle.r$。

“（含 $a$ 的陪集）+（含 $b$ 的陪集）= 含 $a+b$ 的陪集。”

应当很清楚：$ZZ \/ angle.l 12 angle.r$ 同构于 $ZZ_12$。形式上，这不过是把 FHT 应用于下面的同态：

$phi : ZZ -> ZZ_12$，$phi : k |-> k$ （模 12）。

显然，$"Ker"(phi) = {dots, -24, -12, 0, 12, 24, dots} = angle.l 12 angle.r$。由 FHT：

$ZZ \/ "Ker"(phi) = ZZ \/ angle.l 12 angle.r tilde.eq "Im"(phi) = ZZ_12$。

## 第 29 页 / 51

**同构 $i : ZZ_12 -> ZZ \/ angle.l 12 angle.r$ 的一张图**

（图来自 Visual Group Theory 网站。请对照原幻灯片。）

## 第 30 页 / 51

**有限阿贝尔群**

我们已经看到，有些循环群可以表示成直积，有些则不能。

下面是布置 $ZZ_6$ 的凯莱图的两种方式，使直积结构一目了然：$ZZ_6 tilde.eq ZZ_3 times ZZ_2$。（见原图）

然而，群 $ZZ_8$ 不能写成直积。无论我们如何画凯莱图，都必须有一个阶为 8 的箭头。（为什么？）

我们将回答何时 $ZZ_n times ZZ_m tilde.eq ZZ_(n m)$，并由此完全分类所有有限阿贝尔群。

## 第 31 页 / 51

**有限阿贝尔群**

**命题**
$ZZ_(n m) tilde.eq ZZ_n times ZZ_m$ 当且仅当 $gcd(n, m) = 1$。

**证明（梗概）**
“$arrow.l.double$”：假设 $gcd(n, m) = 1$。我们断言 $(1, 1) in ZZ_n times ZZ_m$ 的阶是 $n m$。

$|(1, 1)|$ 是使“$(k, k) = (0, 0)$”成立的最小的 $k$。这件事发生当且仅当 $n | k$ 且 $m | k$。
因此 $k = "lcm"(n, m) = n m$。

（右图示意 $ZZ_4 times ZZ_3 tilde.eq ZZ_12$。见原图。）

## 第 32 页 / 51

**有限阿贝尔群**

**命题**
$ZZ_(n m) tilde.eq ZZ_n times ZZ_m$ 当且仅当 $gcd(n, m) = 1$。

**证明（续）**
“$arrow.r.double$”：假设 $ZZ_(n m) tilde.eq ZZ_n times ZZ_m$。则 $ZZ_n times ZZ_m$ 有一个阶为 $n m$ 的元素 $(a, b)$。
为方便起见，我们将改用“乘法记号”，并把循环群记作 $C_n$。

显然 $angle.l a angle.r = C_n$ 且 $angle.l b angle.r = C_m$。让我们看一看 $C_n times C_m$ 的凯莱图（见原图中的网格）。

$(a, b)$ 的阶必须是 $n$（行数）的倍数，也必须是 $m$（列数）的倍数。
由定义，这就是 $n$ 与 $m$ 的最小公倍数。
但 $|(a, b)| = n m$，因此 $"lcm"(n, m) = n m$。从而 $gcd(n, m) = 1$。证毕。

## 第 33 页 / 51

**有限阿贝尔群基本定理**

**分类定理（按“素数幂”）**
每一个有限阿贝尔群 $A$ 都同构于循环群的直积，也就是说，对某些整数 $n_1, n_2, dots, n_m$，

$A tilde.eq ZZ_(n_1) times ZZ_(n_2) times dots.c times ZZ_(n_m)$，

其中每个 $n_i$ 都是素数幂，即 $n_i = p_i^(d_i)$，这里 $p_i$ 是素数且 $d_i in NN$。

这一定理的证明更为深入，虽然仍属于本科水平，但我们还没有做它所需要的工具。

不过，我们将更关心理解和运用这一结果。

**例子**
在同构意义下，阶为 $200 = 2^3 dot 5^2$ 的阿贝尔群有 6 个：

$ZZ_8 times ZZ_25$，　$ZZ_8 times ZZ_5 times ZZ_5$，

$ZZ_2 times ZZ_4 times ZZ_25$，　$ZZ_2 times ZZ_4 times ZZ_5 times ZZ_5$，

$ZZ_2 times ZZ_2 times ZZ_2 times ZZ_25$，　$ZZ_2 times ZZ_2 times ZZ_2 times ZZ_5 times ZZ_5$。

## 第 34 页 / 51

**有限阿贝尔群基本定理**

有限阿贝尔群也可以按它们的“初等因子”来分类。这一神秘用语来自模的理论（一个研究生水平的课题）。

**分类定理（按“初等因子”）**
每一个有限阿贝尔群 $A$ 都同构于循环群的直积，也就是说，对某些整数 $k_1, k_2, dots, k_m$，

$A tilde.eq ZZ_(k_1) times ZZ_(k_2) times dots.c times ZZ_(k_m)$，

其中每个 $k_i$ 都是 $k_(i+1)$ 的倍数。

**例子**
在同构意义下，阶为 $200 = 2^3 dot 5^2$ 的阿贝尔群有 6 个：

- 按“素数幂” / 按“初等因子”：
- $ZZ_8 times ZZ_25$　对应　$ZZ_200$
- $ZZ_4 times ZZ_2 times ZZ_25$　对应　$ZZ_100 times ZZ_2$
- $ZZ_2 times ZZ_2 times ZZ_2 times ZZ_25$　对应　$ZZ_50 times ZZ_2 times ZZ_2$
- $ZZ_8 times ZZ_5 times ZZ_5$　对应　$ZZ_40 times ZZ_5$
- $ZZ_4 times ZZ_2 times ZZ_5 times ZZ_5$　对应　$ZZ_20 times ZZ_10$
- $ZZ_2 times ZZ_2 times ZZ_2 times ZZ_5 times ZZ_5$　对应　$ZZ_10 times ZZ_10 times ZZ_2$

## 第 35 页 / 51

**有限生成阿贝尔群基本定理**

只是为了好玩，这里给出所有有限生成阿贝尔群的分类定理。注意它并没有太大不同。

**定理**
每一个有限生成阿贝尔群 $A$ 都同构于循环群的直积，也就是说，对某些整数 $n_1, n_2, dots, n_m$，

$A tilde.eq ZZ times dots.c times ZZ times ZZ_(n_1) times ZZ_(n_2) times dots.c times ZZ_(n_m)$，

其中前面有 $k$ 个 $ZZ$ 的副本，并且每个 $n_i$ 都是素数幂，即 $n_i = p_i^(d_i)$，这里 $p_i$ 是素数且 $d_i in NN$。

换句话说，$A$ 同构于一个具有如下表现的（乘法）群：

$A = angle.l a_1, dots, a_k, r_1, dots, r_m mid(|) r_i^(n_i) = 1, a_i a_j = a_j a_i, r_i r_j = r_j r_i, a_i r_j = r_j a_i angle.r$。

总之，（有限生成的）阿贝尔群相对容易理解。

相比之下，非阿贝尔群更为神秘而复杂。不久我们将研究西罗定理，它们将帮助我们更好地理解有限非阿贝尔群的结构。

## 第 36 页 / 51

**同构定理**

基本同态定理（FHT）是关于同态及其结构的四条基本定理中的第一条。

这些定理通常称为“同构定理”：

- 第一同构定理：“基本同态定理”
- 第二同构定理：“菱形同构定理”
- 第三同构定理：“新生定理”（Freshman Theorem）
- 第四同构定理：“对应定理”

所有这些定理在其他代数结构中都有类似物：环、向量空间、模，以及李代数，等等。

在这一讲中，我们将概述后三个同构定理，并为每一个提供视觉图像。

我们将证明其中一个，概述另一个的证明（家庭作业！），并鼓励你尝试最后一个的多个部分的（非常直接的）证明。

最后，我们将引入换位子与换位子群的概念，对它取商就得到一个群的阿贝尔化。

## 第 37 页 / 51

**第二同构定理**

**菱形同构定理**
设 $H <= G$，且 $N lt.tri.eq G$。则（见原图中的菱形）

1. 乘积 $H N = {h n mid(|) h in H, n in N}$ 是 $G$ 的一个子群。
2. 交 $H inter N$ 是 $H$ 的一个正规子群。（原幻灯片写作 “of $G$”；标准陈述是：$H inter N lt.tri.eq H$。）
3. 下列商群同构：$H N \/ N tilde.eq H \/ (H inter N)$。

**证明（梗概）**
定义如下映射

$phi : H -> H N \/ N$，$phi : h |-> h N$。

若我们能证明：

1. $phi$ 是同态，
2. $phi$ 是满射（到上），
3. $"Ker" phi = H inter N$，

则结果将立即由 FHT 得到。细节留作家庭作业。

## 第 38 页 / 51

**第三同构定理**

**新生定理**
考虑 $G$ 的正规子群链 $N <= H <= G$。则

1. 商 $H \/ N$ 是 $G \/ N$ 的一个正规子群；
2. 下列商同构：$(G \/ N) \/ (H \/ N) tilde.eq G \/ H$。

（示意图把 $G$、$H$、$N$ 画成“分数”，形象地表示约分。概念与图像承蒙玻伊西州立大学的 Zach Teitler 提供。）

## 第 39 页 / 51

**第三同构定理**

**新生定理**
考虑 $G$ 的正规子群链 $N <= H <= G$。则 $H \/ N lt.tri.eq G \/ N$，且 $(G \/ N) \/ (H \/ N) tilde.eq G \/ H$。

**证明**
容易证明 $H \/ N lt.tri.eq G \/ N$（习题）。定义映射

$phi.alt : G \/ N -> G \/ H$，$phi.alt : g N |-> g H$。

- 证明 $phi.alt$ 是良好定义的：假设 $g_1 N = g_2 N$。则对某个 $n in N$ 有 $g_1 = g_2 n$。但因为 $N <= H$，有 $n in H$。因此 $g_1 H = g_2 H$，即 $phi.alt(g_1 N) = phi.alt(g_2 N)$。
- $phi.alt$ 显然是到上的，并且是同态。
- 应用 FHT：

$"Ker" phi.alt = {g N in G \/ N mid(|) phi.alt(g N) = H} = {g N in G \/ N mid(|) g H = H} = {g N in G \/ N mid(|) g in H} = H \/ N$。

由 FHT，$(G \/ N) \/ "Ker" phi.alt = (G \/ N) \/ (H \/ N) tilde.eq "Im" phi.alt = G \/ H$。证毕。

## 第 40 页 / 51

**第四同构定理**

完整的陈述有一点技术性，所以这里我们只非正式地叙述它。

**对应定理**
设 $N lt.tri.eq G$。在 $G \/ N$ 的子群与 $G$ 中含 $N$ 的子群之间存在一一对应。特别地，$G \/ N$ 的每一个子群都具有形式 $overline(A) := A \/ N$，其中 $A$ 满足 $N <= A <= G$。
这意味着相应的子群格在结构上是相同的。

**例子**
$Q_8 \/ angle.l -1 angle.r$ 同构于 $V_4$。子群格可以通过把 $angle.l -1 angle.r$ “坍缩”到单位元来可视化。（见原图）

## 第 41 页 / 51

**对应定理（正式陈述）**

设 $N lt.tri.eq G$。则在 $G \/ N$ 的子群与 $G$ 中含 $N$ 的子群之间存在双射。特别地，$G \/ N$ 的每一个子群都具有形式 $overline(A) := A \/ N$，其中 $A$ 满足 $N <= A <= G$。此外，若 $A, B <= G$，则

1. $A <= B$ 当且仅当 $overline(A) <= overline(B)$，
2. 若 $A <= B$，则 $[B : A] = [overline(B) : overline(A)]$，
3. $angle.l overline(A), overline(B) angle.r = overline(angle.l A\, B angle.r)$，
4. $overline(A) inter overline(B) = overline(A inter B)$，
5. $A lt.tri.eq G$ 当且仅当 $overline(A) lt.tri.eq G \/ N$。

**例子**
$D_4 \/ angle.l r^2 angle.r$ 的子群格与 $V_4$ 的子群格相对应（见原图）。

## 第 42 页 / 51

**应用：换位子群与阿贝尔化**

我们已经看到如何用 $angle.l 12 angle.r$ 去除 $ZZ$，从而“迫使”所有 12 的倍数变为零。这是构造模 12 整数的一种方法：$ZZ_12 tilde.eq ZZ \/ angle.l 12 angle.r$。

现在，假设 $G$ 是非阿贝尔的。我们希望用它的“非阿贝尔部分”去除 $G$，使它们变为零，并在所得的商中只留下“阿贝尔部分”。

*换位子* 是形如 $a b a^(-1) b^(-1)$ 的元素。由于 $G$ 是非阿贝尔的，存在非单位的换位子：$a b a^(-1) b^(-1) eq.not e$（在 $G$ 中）。

（见原图：当 $a b = b a$ 与当 $a b eq.not b a$ 时凯莱图片段的对比。）

在这种情形下，集合 $C := {a b a^(-1) b^(-1) mid(|) a, b in G}$ 所含的不止单位元。

定义 $G$ 的 *换位子群* $G'$ 为

$G' := angle.l a b a^(-1) b^(-1) mid(|) a, b in G angle.r$。

这是 $G$ 的一个正规子群（家庭作业）。若我们用它去除，就得到一个阿贝尔群！（因为我们杀死了上面所示的每一种“$a b eq.not b a$ 模式”。）

## 第 43 页 / 51

**换位子群与阿贝尔化**

**定义**
$G$ 的 *阿贝尔化* 是商群 $G \/ G'$。这是人们通过“杀掉” $G$ 的所有非阿贝尔部分而得到的群。

在某种意义上，换位子群 $G'$ 是使 $G \/ N$ 为阿贝尔的、$G$ 的最小正规子群 $N$。（注意，$G$ 本身会是“最大的”这样的子群。）

等价地，商 $G \/ G'$ 是 $G$ 的最大阿贝尔商。（注意，$G \/ G tilde.eq angle.l e angle.r$ 会是“最小的”这样的商。）

**换位子群的泛性质**
假设 $f : G -> A$ 是到一个阿贝尔群 $A$ 的同态。则存在唯一的同态 $h : G \/ G' -> A$，使得 $f = h q$：（见原图交换图）

我们说 $f$ “通过”阿贝尔化 $G \/ G'$ 而分解。

## 第 44 页 / 51

**换位子群与阿贝尔化**

**例子**
考虑群 $A_4$ 与 $D_4$。容易验证

$A_4' = angle.l x y x^(-1) y^(-1) mid(|) x, y in A_4 angle.r tilde.eq V_4$，

$D_4' = angle.l x y x^(-1) y^(-1) mid(|) x, y in D_4 angle.r = angle.l r^2 angle.r$。

（子群格见原图。）

由对应定理，$A_4$ 的阿贝尔化是 $A_4 \/ V_4 tilde.eq C_3$，而 $D_4$ 的阿贝尔化是 $D_4 \/ angle.l r^2 angle.r tilde.eq V_4$。
注意 $G \/ G'$ 是阿贝尔的，而且，用任何位于 $G'$ “之上”的正规子群去除 $G$，都将得到一个阿贝尔群。

## 第 45 页 / 51

**自同构**

**定义**
*自同构* 是从一个群到它自身的同构。
$G$ 的全部自同构构成一个群，称为 $G$ 的 *自同构群*，记作 $"Aut"(G)$。

**注记**
- 一个自同构由它把生成元送到何处所确定。
- 自同构必须把生成元送到生成元。特别地，若 $G$ 是循环的，则它决定（所有可能的）生成元集合的一个置换。

**例子**
1. $ZZ$ 有两个自同构：恒等映射，以及映射 $n |-> -n$。因此 $"Aut"(ZZ) tilde.eq C_2$。
2. 对 $phi(1) in {1, 2, 3, 4}$ 的每一种选择，都有一个自同构 $phi : ZZ_5 -> ZZ_5$。因此 $"Aut"(ZZ_5) tilde.eq C_4$ 或 $V_4$。（是哪一个？）
3. $V_4 = angle.l h, v angle.r$ 的一个自同构 $phi$ 由 $h$ 与 $v$ 的像所确定。$phi(h)$ 有 3 种选择，然后 $phi(v)$ 有 2 种选择。因此 $|"Aut"(V_4)| = 6$，所以它要么是 $C_6 tilde.eq C_2 times C_3$，要么是 $S_3$。（是哪一个？）

## 第 46 页 / 51

**$ZZ_n$ 的自同构群**

**定义**
模 $n$ 的整数乘法群，记作 $ZZ_n^*$ 或 $U(n)$，是群

$U(n) := {k in ZZ_n mid(|) gcd(n, k) = 1}$，

其中二元运算是模 $n$ 的乘法。

$U(5) = {1, 2, 3, 4} tilde.eq C_4$，　$U(6) = {1, 5} tilde.eq C_2$，　$U(8) = {1, 3, 5, 7} tilde.eq C_2 times C_2$。

（乘法表见原图。）

**命题（家庭作业）**
$ZZ_n$ 的自同构群是 $"Aut"(ZZ_n) = {sigma_a mid(|) a in U(n)} tilde.eq U(n)$，其中

$sigma_a : ZZ_n -> ZZ_n$，$sigma_a (1) = a$。

## 第 47 页 / 51

**$D_3$ 的自同构**

让我们找出 $D_3 = angle.l r, f angle.r$ 的全部自同构。当我们研究伽罗瓦理论时，会见到一个与此非常相似的例子。

显然，每一个自同构 $phi$ 完全由 $phi(r)$ 与 $phi(f)$ 确定。

由于自同构保持阶，若 $phi in "Aut"(D_3)$，则

$phi(e) = e$，$phi(r) = r$ 或 $r^2$（2 种选择），$phi(f) = f$、$r f$ 或 $r^2 f$（3 种选择）。

因此，$D_3$ 至多有 $2 dot 3 = 6$ 个自同构。

让我们试着定义两个映射：(i) 固定 $r$ 的 $alpha : D_3 -> D_3$，以及 (ii) 固定 $f$ 的 $beta : D_3 -> D_3$：

$alpha(r) = r$，$alpha(f) = r f$；

$beta(r) = r^2$，$beta(f) = f$。

我断言：

- 这两者都定义自同构（请验证！）
- 它们生成六个不同的自同构，从而 $angle.l alpha, beta angle.r = "Aut"(D_3)$。

要确定这个群同构于什么，找出这六个自同构，并做一个群表现和／或乘法表。它是阿贝尔的吗？

## 第 48 页 / 51

**$D_3$ 的自同构**

自同构可以看成是凯莱图的一种重新接线。

图中给出恒等、$alpha$、$alpha^2$、$beta$、$alpha beta$、$alpha^2 beta$ 这六种自同构把 $r$ 与 $f$ 送到何处，以及相应的“重新接线”图。请对照原幻灯片。

## 第 49 页 / 51

**$D_3$ 的自同构**

这里是 $"Aut"(D_3) = angle.l alpha, beta angle.r$ 的乘法表与凯莱图（见原图）。

$"Aut"(D_3) tilde.eq D_3$ 纯粹是巧合。例如，我们已经看到

$"Aut"(ZZ_5) tilde.eq U(5) tilde.eq C_4$，　$"Aut"(ZZ_6) tilde.eq U(6) tilde.eq C_2$，　$"Aut"(ZZ_8) tilde.eq U(8) tilde.eq C_2 times C_2$。

## 第 50 页 / 51

**$V_4 = angle.l h, v angle.r$ 的自同构**

下面的置换都是自同构。图中给出恒等、$alpha$、$alpha^2$、$beta$、$alpha beta$、$alpha^2 beta$ 把 $h$、$v$、$h v$ 送到何处。请对照原幻灯片。

## 第 51 页 / 51

**$V_4 = angle.l h, v angle.r$ 的自同构**

这里是 $"Aut"(V_4) = angle.l alpha, beta angle.r tilde.eq S_3 tilde.eq D_3$ 的乘法表与凯莱图（见原图）。

回想 $alpha$ 与 $beta$ 可以看成 $h$、$v$、$h v$ 上的置换，因此总有 $"Aut"(G) arrow.r.hook "Perm"(G) tilde.eq S_n$。

