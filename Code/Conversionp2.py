Mat src = new Mat();
Mat dstA = new Mat();
Mat dstB = new Mat();
src = Imgcodecs.imread("full.jpg", Imgcodecs.IMREAD_COLOR);

List<Mat> channelsYUVa = new ArrayList<Mat>();
List<Mat> channelsYUVb = new ArrayList<Mat>();

Imgproc.cvtColor(src, dstA, Imgproc.COLOR_BGR2YUV); #convert bgr image to yuv
Imgproc.cvtColor(src, dstB, Imgproc.COLOR_BGR2YUV);

Core.split(dstA, channelsYUVa); #isolate the channels y u v
Core.split(dstB, channelsYUVb);

#zero the 2 channels we do not want to see isolating the 1 channel we want to see
channelsYUVa.set(0, Mat.zeros(channelsYUVa.get(0).rows(),channelsYUVa.get(0).cols(),channelsYUVa.get(0).type()));
channelsYUVa.set(1, Mat.zeros(channelsYUVa.get(0).rows(),channelsYUVa.get(0).cols(),channelsYUVa.get(0).type()));

channelsYUVb.set(0, Mat.zeros(channelsYUVb.get(0).rows(),channelsYUVb.get(0).cols(),channelsYUVb.get(0).type()));
channelsYUVb.set(2, Mat.zeros(channelsYUVb.get(0).rows(),channelsYUVb.get(0).cols(),channelsYUVb.get(0).type()));

Core.merge(channelsYUVa, dstA); #combine channels (two of which are zero)
Core.merge(channelsYUVb, dstB);

Imgproc.cvtColor(dstA, dstA, Imgproc.COLOR_YUV2BGR);  #convert to bgr so it can be displayed
Imgproc.cvtColor(dstB, dstB, Imgproc.COLOR_YUV2BGR);

HighGui.imshow("V channel", dstA); // display the image
HighGui.imshow("U channel", dstB);

HighGui.waitKey(0);
