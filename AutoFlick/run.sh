#!/bin/bash
function chk()
{
	read -p "Loop have finished. Do you want to exit?[y/Y]" ch
	case $ch in
		y|Y)
			echo "Exit!"
			exit 0
			;;
		*)
			monkeyrunner ./AutoTouch.py
			chk
			;;
	esac
}

chk

