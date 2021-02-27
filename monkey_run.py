import subprocess

def run_monkey(count):
    cmd = f'adb shell monkey -v -p com.sina.weibo --throttle 100 -s 1614605682960 {count}'
    subprocess.Popen(cmd, shell=True, stdout=open('./monkey.log', mode='w'))

if __name__ == '__main__':
    run_monkey(100)