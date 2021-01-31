# 项目结构
* pom 页面模型文件
* screenshots 项目截图
* testcases 测试用例
* conftest.py 项目配置文件

# 依赖库
将依赖库保存到 requriements.txt 文件

`pip freeze > requriements.txt`

# 安装依赖库

pip install -r requriements.txt

自动安装requriements.txt文件中定义的所有库

# 运行
`pytest testcases  -v --html=report.html --self-contained-html`
