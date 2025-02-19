<script lang="ts" setup>

import { VueCompareImage } from 'vue3-compare-image';

const inputImagePath = './image_inner/pointcloud.jpg';
const outputImagePath = './image_inner/segment.jpg';


</script>

<template>
  <div>
    <el-divider />

    <el-row justify="center">
      <h1 class="section-title">Point Cloud and Instance Segmentation</h1>
    </el-row>
    <el-row justify="center">
    <div class="el-col el-col-24 el-col-xs-24 el-col-sm-20 el-col-md-20 el-col-lg-16 el-col-xl-12" style="margin-top:20px; color: #4A4A4A;">
      Through the OpenFly platform's toolchain, point clouds for each scene can be collected, enabling semantic segmentation of the entire scene.
    </div>
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

  </div>
</template>

<style scoped>

</style>
