from foaas import fuck
import subprocess

shell = True

def speak(this):
    # print(this)
    this = this.replace("-", "from")
    # print(this)
    subprocess.run(['flite', '-t', this])

speak(str(fuck.random(from_='tinkermind').text))
