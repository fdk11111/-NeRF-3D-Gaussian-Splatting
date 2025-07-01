import sys
print(f"Python 路径: {sys.path}")
try:
    import pyngp
    print("✅ pyngp 导入成功!")
    from pyngp import Testbed
    testbed = Testbed()
    print("✅ Testbed 初始化成功!")
except ImportError:
    print("❌ pyngp 导入失败")
