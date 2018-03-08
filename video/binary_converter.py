from bitstring import BitStream, BitArray

def stream_to_binary(image_file,binary_file):
	b = BitArray(bytes=open(image_file, 'rb').read())
	with open(binary_file,'w') as f:
		f.write(b.bin)

def binary_to_stream(binary_file,image_file):
	bytes=open(binary_file,'r').read()
	d=BitArray(bin=bytes)
	with open(image_file,'wb') as f:
		f.write(d.bytes)

#image_to_binary('image.jpg','binary_image.bin')
#binary_to_image('binary_image.bin','image_op.jpg')

stream_to_binary('vid.mp4','binary_video.bin')
binary_to_stream('binary_video.bin','test_op.mp4')
