# Amazon CloudFront Cache and Behavior Settings

1. Set up Amazon S3 buckets:
- Create two S3 buckets for the files (e.g., 'pdf-bucket' and 'jpg-bucket')
- Upload sample PDF files to the 'pdf-bucket' and JPG images to the 'jpg-bucket'
- Create a bucket for the static website

2. For the static website:
- Enable public access
- Configure as a static website
- Add the index.html (when ready)

3. Configure Amazon CloudFront:
- Create a new CloudFront distribution
- Add the static website as an origin (use website endpoint)
- Disable caching
- Add 2 more origins for the buckets containing the files and create/configure OAC
- Configure cache behavior settings for each origin based on file type (PDF or JPG) and default going to the static website