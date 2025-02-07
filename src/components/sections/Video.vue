<script setup>
const cover = './cover.png'
</script>

<template>
  <div>
    <!-- <el-divider /> -->
    <el-row justify="center">
      <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="10" >
        <el-container class="video-container">
          <!-- <img src="./cover.png" alt="cover" style="width: 100%; height: auto;"> -->
          <el-image :src="cover" class="logo" fit="cover" />
        </el-container>
      </el-col>
    </el-row>

    <!-- <el-divider /> -->
    <el-row justify="center">
      <!-- <h1 class="section-title">Video</h1> -->
    </el-row>

    <!-- 每个网站的视频的iframe可能不一致，最好在这里手动调整 -->
    <el-row justify="center">
      <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="10" >

        <!-- local -->
        <!-- <el-container class="video-container">
          <video controls muted preload playsinline>
            <source src="/video/video.mp4" type="video/mp4">
          </video>
        </el-container> -->
        
        <!-- bilibili -->
        <!-- <el-container class="video-container">
          <iframe src="//www.bilibili.com/blackboard/html5mobileplayer.html?bvid=BV1zw68YsEP9" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
        </el-container> -->

        <!-- youtube -->
        <!-- <el-container class="video-container">
          <iframe src="https://www.youtube.com/embed/wjZofJX0v4M?si=BFvRyc3n3fFV_f1G" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </el-container> -->
      </el-col>
    </el-row>
  </div>

  <el-divider />
  <el-row justify="center">
      <h1 class="section-title">Scene Overview</h1>
  </el-row>

  <iframe src="/openfly/visualizer.html" width="100%" height="550px" style="border: none;"></iframe>
</template>

<style scoped>

.video-container{
  margin: 20px 0px 0px 0px;
}

iframe, video {
  aspect-ratio: 16 / 9;
  width: 100%;
}

</style>