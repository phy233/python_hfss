# coding=utf-8
# 这是一个示例 Python 脚本。

import sys
sys.path.append(r"D:\Program Files\AnsysEM\AnsysEM21.1\Win64")
sys.path.append(r"D:\Program Files\AnsysEM\AnsysEM21.1\Win64\PythonFiles\DesktopPlugin")
sys.path.append(r"D:\Program Files\AnsysEM\AnsysEM21.1\Win64\common\IronPython\Lib")

import ScriptEnv
ScriptEnv.Initialize("AnsoftHfss.HfssScriptInterface")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")

ScriptEnv.Shutdown()


