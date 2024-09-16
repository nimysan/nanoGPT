import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import wandb

# 设置随机种子以确保可重复性
torch.manual_seed(42)
np.random.seed(42)

# 初始化 wandb
wandb.init(project="simple-linear-model", name="experiment-1")

# 生成一些随机数据
X = torch.randn(100, 1)
y = 2 * X + 1 + torch.randn(100, 1) * 0.1


# 定义一个简单的线性模型
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


# 创建模型实例
model = LinearModel()

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
    # 前向传播
    outputs = model(X)
    loss = criterion(outputs, y)

    # 反向传播和优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 记录损失和参数
    wandb.log({
        "epoch": epoch,
        "loss": loss.item(),
        "weight": model.linear.weight.item(),
        "bias": model.linear.bias.item()
    })

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 打印最终的权重和偏置
print(f'Final weight: {model.linear.weight.item():.4f}')
print(f'Final bias: {model.linear.bias.item():.4f}')

# 结束 wandb 运行
wandb.finish()