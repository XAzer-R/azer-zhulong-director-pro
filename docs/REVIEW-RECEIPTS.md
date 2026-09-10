# 审核记录与版本检查

主控完成审核后在作品输出目录保存 JSON；inputs 与 outputs 的键为作品根下的相对文件路径，值为实际文件 SHA-256 小写十六进制。至少各有一个文件。不得填写示例散列或凭空标为 PASS。

字段：status（PASS 或 FAILED）、blockers（问题字符串数组）、inputs（路径到散列的对象）、outputs（路径到散列的对象）。

继续下游前调用 tools/workflow_guard.py review。仅 CURRENT 且用户范围允许才可继续；BLOCKED 停止修订决策，STALE 重新核验当前版本。工具退出码 0 为当前通过，1 为阻断或失效，2 为无效输入。

该记录只服务本地流程一致性，不是数字签名；有文件写权限的人也可以修改审核记录。艺术质量与人工最终判断不能由 hash 证明。
