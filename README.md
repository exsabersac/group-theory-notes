# 群论学习资源与笔记

从零开始系统学习**群论**的资源索引、推荐学习路径，以及少量原创笔记骨架。面向刚学到「群的定义」的读者，以**简体中文资源为优先**，英文材料放在后面作补充。

本仓库不是教材正文的转载，也**不提供任何商业教材的扫描件或来路不明的电子书**。丘维声、张禾瑞、石生明、韩士安 / 林磊、冯克勤、聂灵沼 / 丁石孙、徐明曜、Artin *Algebra*、Carter *Visual Group Theory* 等，请自行购买纸书或电子正版。所列条目均为出版社书目、院校公开课、作者公开讲义或已声明许可的开源笔记。部分官方开放的 PDF 已放入 [pdfs/](pdfs/README.md)，并保留原站链接与许可说明。

## 建议怎么用

1. 先读 [学习路径](学习路径.md)，按阶段推进，不要一上来同时开很多本书。
2. 选定**一本主教材 + 一门系统视频课**，其余资源只作对照或查缺。
3. 从本仓库的 [笔记：群的定义](notes/01-群的定义.md) 核对基本概念，再自己动手补例子与证明。
4. 需要可视化直觉时，可配合 [*Visual Group Theory* 相关资料](resources/Visual-Group-Theory.md) 与 Group Explorer。Macauley 章节幻灯片的非官方中译对照本在 [translations/macauley-vgt/](translations/macauley-vgt/)（原图在上、中文在下）。
5. 离线阅读请看 [pdfs/](pdfs/README.md)：现有 Judson 开放教材、Milne 与 Conrad 讲义、MIT OCW 群论讲义、Ernst 的 IBL 教材，以及 *Visual Group Theory* 的官方样章与 Macauley / Ernst 公开讲义。中文系统讲义目前多是网页（如交大高云），没有官方 PDF，请到原站阅读。

当前推荐的「一条主线」（均可合法公开获取课程或购买纸书）：

- 教材：丘维声《[抽象代数基础（第 2 版）](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=59cef680ba9eb884cf81fc1c)》（群的一章已覆盖到作用、Sylow 与有限交换群），或张禾瑞《[近世代数基础（第三版）](https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=669d417874ce561611bda259)》（起点更慢，适合完全零基础）。
- 视频：中国大学 MOOC [南京大学《近世代数》](https://www.icourse163.org/course/NJU-1462062161)（孙智伟讲授群论前 18 讲；2025 年入选国家级一流本科课程）。

## 目录

| 文档 | 内容 |
| --- | --- |
| [学习路径](学习路径.md) | 从群的定义到结构定理的阶段划分、每阶段该读什么 |
| [中文教材与习题书](resources/中文教材.md) | 经典教材与习题集，均链到出版社或正规书目页 |
| [中文讲义、笔记与课程大纲](resources/中文讲义与笔记.md) | 院校公开讲义、开源笔记、课程指南 |
| [中文视频课程](resources/中文视频.md) | 慕课、学堂在线、B 站完整课程（优先系统课） |
| [英文补充](resources/英文补充.md) | 免费讲义、公开课与可视化工具（英文） |
| [Visual Group Theory 相关资料](resources/Visual-Group-Theory.md) | Carter 的书、官方样章、Macauley 视频课与讲义、Group Explorer |
| [Macauley 讲义非官方中译](translations/macauley-vgt/) | 7 章幻灯片对照 PDF（原图 + 简体中文，CC BY-NC-SA 4.0） |
| [与范畴论 / 编程的衔接](resources/范畴论与编程衔接.md) | 群作为单对象群胚、Haskell 中的 `Group`；不是主线 |
| [拓扑学资源](resources/拓扑.md) | 点集拓扑与代数拓扑的精选索引（邻近学科，不是第二条主线） |
| [笔记骨架](notes/README.md) | 从「群的定义」开始的简短原创笔记 |
| [pdfs/](pdfs/README.md) | 官方公开、许可允许保存的 PDF 离线副本（含来源与许可） |

## 许可

本仓库中的**原创文字**（学习路径、注解、笔记骨架等）以 [CC BY 4.0](LICENSE) 发布。你可以使用、改编，只需署名并给出本仓库链接。

链出的教材、课程、讲义与视频**保留各自版权与许可**，不因被收入本索引或 `pdfs/` 而改变。开放教材与讲义的本地副本遵循其原许可（如 GNU FDL、CC BY-SA、CC BY-NC-SA）；开源笔记条目会另行标明其原许可（如 Apache-2.0、CC BY 4.0）。

[translations/macauley-vgt/](translations/macauley-vgt/) 中的 Macauley 讲义中译本是原课程材料的演绎作品，以 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 发布，不是本仓库原创文字所用的 CC BY 4.0。

## 维护说明

条目在 2026 年 11 月收集，并尽可能用 HTTP 请求核对到课程页、书目页或可播页。若某链接失效，欢迎发 Issue 或 Pull Request。不收录来源不明的网盘文件或未授权扫描件。
