# 在 ngp-workspace 目录创建 restore_model.py
import os
import pyngp as ngp

# 初始化测试环境
testbed = ngp.Testbed()
testbed.root_dir = "/root/autodl-tmp/ngp-workspace"

# 加载数据集（重要！必须与训练时相同）
testbed.load_training_data("data/mydata")

# 重建模型状态（无需重新训练）
testbed.reload_network_from_cache()

# 强制造模（修复开发版缺陷）
testbed.apply_model_reconstruction_fix()

# 保存最终模型
save_path = "recovered_final_model.msgpack"
testbed.save_snapshot(save_path, False)

print(f"✅ 模型已成功恢复至: {save_path}")
print(f"⚡ 模型大小: {os.path.getsize(save_path)/1e6:.2f} MB")