<script lang="ts" setup>

import { VueCompareImage } from 'vue3-compare-image';

const inputImagePath = './image_inner/pointcloud.jpg';
const outputImagePath = './image_inner/segment.jpg';
const videos = [
  {
    src: 'video/success_case/0.mp4'
  },
  {
    src: 'video/success_case/1.mp4'
  },
  {
    src: 'video/success_case/3.mp4'
  },
  {
    src: 'video/success_case/5.mp4'
  },
  {
    src: 'video/success_case/6.mp4'
  },
  {
    src: 'video/success_case/7.mp4'
  }
];

</script>

<template>
  <div>
    <el-divider />

    <el-row justify="center">
      <h1 class="section-title">Point Cloud and Instance Segmentation</h1>
    </el-row>

    <el-row justify="center">
        <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="12">
            <el-row style="margin-top: 20px;" >
                <VueCompareImage 
                    :left-image="inputImagePath" 
                    :right-image="outputImagePath"
                    :hover="true"
                />
            </el-row>
        </el-col>
    </el-row>

    <el-divider />
    <el-row justify="center">
      <h1 class="section-title">Success Examples</h1>
    </el-row>

    <el-row justify="center">
      <!-- add video player -->
      <el-col :xs="24" :sm="20" :md="20" :lg="16" :xl="12" >
        <el-row justify="center" style="margin-top: 20px;">
          <el-col v-for="(video, index) in videos" :key="index" :span="12" style="padding: 0 10px;">
            <video :src="video.src" controls style="width: 100%;"></video>
          </el-col>
        </el-row>
      </el-col>
    </el-row>

  </div>
</template>

<style scoped>

</style>
