clear all;
clc;
for n=1:16

image_{n}= imread(sprintf('%s.jpg',num2str(n)));
threshold = 128;
Igray = rgb2gray(image_{n});
Ibw = Igray>threshold;
imshow(Ibw);
imwrite(Ibw,sprintf('b%s.jpg',num2str(n)));
end

%Irgb = imread('Brown/16.jpg');
% threshold = 128;
% Igray = rgb2gray(Irgb);
% Ibw = Igray>threshold;
%imshow(Ibw);
%imwrite(Ibw,'b16.jpg');