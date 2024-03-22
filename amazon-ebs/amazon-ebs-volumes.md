# Amazon EBS Volume Lab

## Launch Instances in two AZs

1. Launch an instance using the Amazon Linux AMI in us-east-1a
2. Launch another instnace using the Amazon Linux AMI in us-east-1b

## Create and Attach an EBS Volume
1. Create a 10GB gp2 volume in us-east-1a with a name tag of 'data-volume'
2. List non-loopback block devices on instance
sudo lsblk -e7
3. Attach the volume to the instance in us-east-1a
4. Rerun the command to view block devices

## Create a filesystem and mount the volume
1. Create a filesystem on the EBS volume
sudo mkfs -t ext4 /dev/xvdf
2. Create a mount point for the EBS volume
sudo mkdir /data
3. Mount the EBS volume to the mount point
sudo mount /dev/xvdf /data
4. Make the volume mount persistent
Run: 'sudo nano /etc/fstab' then add '/dev/xvdf /data ext4 defaults,nofail 0 2' and save the file

## Add some data to the volume

1. Change to the /data mount point directory
2. Create some files and folders

## Take a snapshot and move the volume to us-east-1b

1. Take a snapshot of the data volume
2. Create a new EBS volume from the snapshot in us-east-1b
3. Mount the new EBS volume to the instance in us-east-1b
4. Change to the /data mount point and view the data

