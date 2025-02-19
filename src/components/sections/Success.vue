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
      <h1 class="section-title">Successful Examples</h1>
    </el-row>
    <el-row justify="center">
      <div class="el-col el-col-24 el-col-xs-24 el-col-sm-20 el-col-md-20 el-col-lg-16 el-col-xl-12" style="margin-top:20px; color: #4A4A4A;">
        The OpenFly platform proposes OpenFly-Agent, a keyframe-aware  VLN model that integrates language instructions, current observations,  and historical keyframes to directly generate flight actions.
      </div>
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
