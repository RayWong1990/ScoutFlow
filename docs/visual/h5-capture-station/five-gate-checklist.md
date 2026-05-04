# ScoutFlow H5 Capture Station 5 Gate Checklist

本清单用于后续 still、prototype、和真实页面的视觉验收。5 项必须全过，任何一项不过都不能把视觉结果叫做通过。

## Gate 1 - 视觉层级

- 用户 3 秒内必须看出第一注意点是 `URL Bar + Capture Action`
- `Live Metadata` 的主值要明显强于次级注释
- `Trust Trace` 是深度检查区，但不能抢走首屏主操作

Reject signals:

- 4 面板同时抢主视觉
- 标题、副标题、关键值权重过于接近

## Gate 2 - 空间对齐

- 4 面板边界必须共享清晰栅格
- lower grid 的列宽和留白要稳定
- 图表、标题、数值行必须沿共同对齐线落位

Reject signals:

- panel 内部边距不一致
- graph、state list、metadata 行各自漂移

## Gate 3 - 遮挡安全

- 任何 badge、legend、toast、tooltip 都不能压住主 URL、主标题、关键 state、或信任链节点标签
- mobile safe area 不能吃掉底部关键信息
- blocked lane 标识不能覆盖真实当前状态

Reject signals:

- overlay 盖住标题或关键数值
- graph 细节层遮住主节点标签

## Gate 4 - 字体可读

- station title、panel title、metadata 主值、secondary text 应保持清晰等级差
- machine strings 需要可换行或安全截断
- 对比度必须支撑长时间扫描

Reject signals:

- panel title 和正文几乎同级
- URL、ID、时间戳因字重/对比问题难读

## Gate 5 - 视觉重量

- 主动作、当前 state、活跃 trust-trace path 的重量必须高于 blocked/future lanes
- blocked lane 要可见，但不能像当前已解锁能力
- 右侧 graph 虽然更宽，但不能压过 URL 行的主操作位

Reject signals:

- blocked lane 颜色/对比度超过当前 active lane
- 图形装饰比真实状态更抢眼
