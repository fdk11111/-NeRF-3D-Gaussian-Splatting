NeRF 与 3D Gaussian Splatting 项目

本项目实现了神经辐射场（NeRF）和3D Gaussian Splatting技术，用于从多视角图像重建和渲染3D场景。该项目包含完整的训练管道、可视化工具和评估脚本。

📂 项目结构

scripts/                  # 核心训练和渲染脚本

  ├── run.py                 # 主训练脚本
  └── colmap2nerf.py         # COLMAP到NeRF格式转换
configs/                  # 训练配置文件

docs/                     # 实验报告和视频演示

.gitignore                # 文件排除规则

README.md                 # 项目文档（本文件）

requirements.txt          # Python依赖库

🚀 快速开始

环境配置

conda create -n nerf-gaussian python=3.8
conda activate nerf-gaussian
pip install -r requirements.txt

训练NeRF模型

python scripts/run.py \
  --scene /path/to/dataset \
  --n_steps 40000 \
  --save_snapshot model.msgpack

渲染360°视频

python scripts/run.py \
  --load_snapshot model.msgpack \
  --video_camera_path camera_path.json \
  --video_output render.mp4

🔧 数据集准备

我们使用以下数据集格式：

your_dataset/
├── images/     # 多视角图片 (JPG/PNG)
└── transforms.json  # 相机参数文件

数据集下载
数据集 描述 下载链接

自定义数据集 本项目使用的数据集 https://pan.baidu.com/share/init?surl=3lx8MNC1zaSMbXwjVD_PxQ&pwd=15ga 
Fox 预训练 NeRF官方示例 https://github.com/NVlabs/instant-ngp

💾 预训练模型
模型 描述 下载地址

NeRF模型 40000步训练结果 百度网盘链接中
3D Gaussian 自定义物体模型 百度网盘链接

📈 实验结果

定量评估（PSNR）
方法 PSNR (db) 训练时间

NeRF 28.7 32分钟
Instant-NGP 27.3 13分钟
3D Gaussian 31.2 46分钟

渲染示例

!docs/render_preview.gif

详细结果见：docs/experiment_report.pdf

❓ 常见问题
数据集准备问题

Q: 如何生成相机参数文件？  
A: 使用提供的colmap2nerf.py脚本：
python scripts/colmap2nerf.py --images /path/to/images

模型训练失败

Q: 训练时出现CUDA内存不足错误  
A: 尝试减少分辨率：
python scripts/run.py ... --width 640 --height 480

渲染质量问题

Q: 渲染视频不够清晰  
A: 增加渲染采样：
python scripts/run.py ... --spp 32

📬 反馈与贡献

欢迎提交issue或PR！本项目遵循以下准则：
使用GitHub issue报告问题

提交PR前运行格式化工具：black scripts/

项目负责人: Feng Dingkang  
联系邮箱: tonyfeng0001@gmail.com  
项目仓库: https://github.com/fdk11111/-NeRF-3D-Gaussian-Splatting  

请注意：由于数据集和模型文件较大（>100MB），它们存储在外部云盘中。请使用上文提供的链接下载这些资源。本仓库仅包含可复现研究结果所需的代码和文档。
