import os
import sys

def main():
	os.system('sudo dscacheutil -flushcache')
	os.system('sudo killall -HUP mDNSResponder')



if __name__ == '__main__':
	main()