## 学习方法
- 访问官网
- github
- 看例子和单元测试
## Flink的变成模型
- 对接数据源 ==> 使用引擎进行业务处理 ==> 结果写到某个地方去
- MR：InputFormat ==> Mappper ==> Reducer ==> ...
- Hive: Table(s) ==> SQL ==> insert
- Spark: RDD/DF/DS ==> Transformation ==> Action/Output
- Flink：Source ==> Transformation ==> Sink
## Flink的架构组成
- JobManager 需要HA
- TaskManager 多个的
- FlinkClient 
## Flink 基础API
- StreamExecutionEnvironment
- Source API
- Transformation API
- Sink API
## 关于Source的API
- 可以实现sourceFunction来实现自定时source 但是并行度为1
- 实现ParallelSourceFunction 可以自动控制并行度
- 实现RichParallelSourceFunction 可以实现
- env接入soucre并行使用 env.fromParallelCollection(new NumberSequenceIterator(1,10),Long.class)
## 关于Transformation
- map算子 DataStream -> DataStream 对每一个元素进行操作变成另外一个元素 整体上是1->1
- flatMap 一个元素进来可以拆成多个元素出去
- Filter 集合进来过滤掉相应元素出去
- KeyBy DataStream -> KeyedStream
- Reduce KeyedStream → DataStream 
- Window KeyedStream → WindowedStream
## 关于sink的API
## Flink实时处理核心API
- Flink Function宏观层次
- 自定义source
- Transformation算子高级篇
- 自定义分区器
- 自定义sink
## 自定义source
- RichSourceFunction
## Flink时间语义及Window API篇
- Flink时间语义
- window基本概念
- window类型
- 基于window编程
- WindowFunction
## 时间语义的内容
- EventTime event/数据真真正正产生的时间 执行结果肯定是确定的 乱序、延迟数据
- IngestionTime event/数据对接到Flink的时间
- ProcessingTime event/进行Flink运算的时间 与算子的执行时间是有必然关系的  性能好、延迟低 不确定性
## 流定义
- 无界流
- window
- - 分类 是否keyBy 按照key进行分组 stream.keyBy(..).window(..)
- - stream.windowAll
- - 时间 窗口大小[start,end) 与数量无关
- - 数量 元素个数 与时间无关 
## Flink WaterMark
Watermark
    结合EventTime进行操作
    数据的延迟==>数据到Flink可能会产生乱序问题
    Window：[00,05)
         何时关闭Windows,然后进行计算
         机制：我们自己可以设定一个 
## Flink state管理
- 状态能为我们带来什么
- - state
- 状态的分类
- 状态的开发
- checkpoint
- 重启策略
- statebackend
- savepoints
## checkpoint 存储
- MemoryStateBackend -先存在taskmanger 在周期性把内存信息发到jobManger
- MemoryStateBackend 异步快照
- FsStateBackend
- RocksDBStateBackend