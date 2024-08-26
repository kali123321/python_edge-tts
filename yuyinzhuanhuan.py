# 还有bug ，有几处还需优化，输入检测部分存在缺陷
import asyncio
from edge_tts import Communicate
import subprocess
import re

# 创建字符切割函数,暂时用不到留着以备以后做优化
#def split_string_by_spaces_to_newline(text):
#    pattern = r"\s([^\n]*)"
#    matches = re.findall(pattern, text)

#    return [match for match in matches if match.strip()]

# 创建提取第一个元素函数，暂时用不到，留着做优化
#def get_first_element(lst):
#    return lst[0] if lst else None

#创建转换函数
async def main(test, Madols, filename):
    communicate = Communicate(test, Madols)
    await communicate.save(filename)

#创建语音列表遍历函数
def list_edge_tts_voices():
    #运行edge-tts命令以列出所有语音
    process = subprocess.Popen(['edge-tts', '--list-voices'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    #将输出分割为一个列表，每个条目代表一个语音
    voices = output.decode().strip().split('\n')
    #遍历打印每个语音
    for voice in voices:
        print(voice)
    return voices
print('===============================================')
print('输入文本时：\n 只键入 exit 将会退出程序')
print('只键入 huanren 将会进入语音模型选择')
print('程序输出20个语音文件会自动退出，防止溢出')
print('注意 ：语音模型name输入格式固定，建议直接复制粘贴\n格式例如：zh-CN-XiaoxiaoNeural(区分大小写)')
print('语音模型默认值：zh-CN-XiaoxiaoNeural')
print('===============================================')
i = 1
# 语音模型默认值
Madol = "zh-CN-XiaoxiaoNeural"
while True:
    Test = input('请输入文本(输入huanren切换语音):')
    Filename = f"nu_{i}.mp3"
    # 条件满足显示语音选项
    if Test == "huanren" :
        liebiaos = list_edge_tts_voices()
        # 查看输入是否符合条件
        Madol = input('请输入语音模型(区分大小写)Name:')
        restart = True
        while restart:
            restart = False
            for liebiao in liebiaos:
                if Madol.count("-") >= 2 and "Neural" in Madol and Madol  in liebiao:
                    restart = False
                    break
            if restart != False:
                Madol = input('输入有误，请重新输入name：')
    if Test == "huanren":
        continue

    if Test == "exit":
        break
    #下面这个if防止死循环溢出，20代表可以输出20个文件，数量可调。
    if i >= 20 :
        break
    #下面两行是主要执行代码，尽量不动。
    if __name__=="__main__":
        asyncio.run(main(Test, Madol, Filename))
    #以下print函数可更改
    print('================================')
    print('转换成功！')
    print(f'这是本次转换的第 {i} 个文件\n文件名：{Filename}')
    print('================================')
    i += 1
    print(f'\n开始第{i}次转换：(输入exit可退出程序)')

print('程序已经结束！')
exit()
