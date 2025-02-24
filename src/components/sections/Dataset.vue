<script setup>
const dataset = './dataset.jpg';
</script>
<template>
  <el-divider />
  <el-row justify="center">
      <h1 class="section-title">Dataset Overview</h1>
  </el-row>
    <el-row justify="center" style="margin-top: 20px;">
      <el-col :xs="24" :sm="24" :md="20" :lg="16" :xl="12" >
        <el-container class="video-container">
          <!-- <img src="./cover.png" alt="cover" style="width: 100%; height: auto;"> -->
          <el-image :src="dataset"  style="width: 100%; height: auto;" fit="cover" />
        </el-container>
      </el-col>
    </el-row>
    <!-- <el-row justify="center">
      <div class="el-col el-col-24 el-col-xs-24 el-col-sm-20 el-col-md-20 el-col-lg-16 el-col-xl-12" style="margin-top:20px; color: #4A4A4A;">
        Framework of the automatic data generation platform. Various rendering engines and simulators are first integrated, providing diverse high-quality scenes. Built on these, several interfaces and tools are developed, enabling automated generation of trajectories and instructions.
      </div>
    </el-row> -->

</template>

  