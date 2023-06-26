1. vscode安装ssh插件，ssh方式进入内核源码目录

2. vscode安装clangd插件(在连上远程ssh下安装)

3. 在内核源码下新建.vscode目录(主要是配置文件)，下载vscode-linux-kernel脚本工具到此目录。
   在源码根目录运行$ python .vscode/generate_compdb.py生成compile_commands.json文件

4. linux服务器安装clang环境，直接apt安装clang>12的版本，然后安装clangd

5. .vscode里面注意添加langd的路径
