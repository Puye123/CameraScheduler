#!/usr/bin/env bash


echo "copy CamSheduler conf"
sudo cp ./cam_scheduler.service /etc/systemd/system/.

sudo systemctl daemon-reload
sudo systemctl enable cam_scheduler.service

sudo systemctl restart cam_scheduler.service
sudo systemctl status cam_scheduler.service

