output_dir="/media/fabifuu/A. Kafa B.//media/fabi/A. Kafa B./Thesis Research/Experiment/3. Cell-IQ (CQ)/20230915 - CQ22 3D/Videos/"
for dir in "/media/fabifuu/A. Kafa B./Thesis Research/Experiment/3. Cell-IQ (CQ)/20230804 - CQ21 2D (AZD, Metf)/JPEG outline/"*; do
  if [ -d "${dir}" ]; then
    dir_name=$(basename "$dir")
    ffmpeg -framerate 5 -pattern_type glob -i "${dir}/*.jpg" -s hd1080 -pix_fmt yuv420p -vcodec libx264 "${output_dir}/${dir_name}.mp4"
  fi
done

