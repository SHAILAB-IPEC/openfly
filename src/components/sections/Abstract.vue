<script setup>
import abstract from '../mds/abstract.mdx';
</script>

<template>
  <div>
    <el-divider />

    <el-row justify="center">
        <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="12">
            <abstract />
        </el-col>
    </el-row>

    <el-divider />
    <el-row justify="center">
      <h1 class="section-title">Video</h1>
    </el-row>


    <!-- 每个网站的视频的iframe可能不一致，最好在这里手动调整 -->
    <el-row justify="center" style="margin-top: 20px;">
      <el-col :xs="24" :sm="20" :md="20" :lg="16" :xl="12" >
        <video controls preload playsinline style="width: 100%;">
          <source src="/video/demo.mp4" type="video/mp4">
        </video>
      </el-col>
    </el-row>

  </div>
</template>

<style scoped>

</style>