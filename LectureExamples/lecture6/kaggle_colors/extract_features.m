function [ X,y ] = extract_features(original_images_file,masked_images_file)

[originals]=textread(original_images_file,'%s','delimiter','\n');
[maskeds]=textread(masked_images_file,'%s','delimiter','\n');

labels=zeros(80,1);
j=1;
X = [];
y = [];
feature_iteration = 1;
sample_dimension = 1;
moment_image = [];

for i=1:160

    if mod(i,2)~=0
    original=char(originals(i));
    
    [image]=strsplit(original,' ');
    image_file=char(image(1));
    labels(j)=str2num(char(image(2)));
   
    
    masked=char(maskeds(i));

    masked_image=imread(masked);
   original_image=imread(image_file);
     
  
     for a=1:100:size(masked_image,1)
            for b=1:100:size(masked_image,2)
                if masked_image(a,b,1) == 255
                    moment_image(sample_dimension,1,1) = original_image(a,b,1);
                    moment_image(sample_dimension,1,2) = original_image(a,b,2);
                    moment_image(sample_dimension,1,3) = original_image(a,b,3);
                    sample_dimension = sample_dimension + 1;
                    if sample_dimension == 25
                        sonuc_moment = color_moments(moment_image);
                        X(feature_iteration,1) = sonuc_moment(1); 
                        X(feature_iteration,2) = sonuc_moment(2); 
                        X(feature_iteration,3) = sonuc_moment(3); 
                        X(feature_iteration,4) = sonuc_moment(4); 
                        X(feature_iteration,5) = sonuc_moment(5); 
                        X(feature_iteration,6) = sonuc_moment(6); 
                        y(feature_iteration,1) =labels(j);
                        feature_iteration = feature_iteration + 1;
                        sample_dimension = 1;
                        moment_image = [];
                    end
                end
            end
        end
    j=j+1;
   
    end
end

end

