<script setup>

</script>

<template>
  <div>
    <el-divider />
    <el-row justify="center">
        <h1 class="section-title">Trajectory Generation</h1>
    </el-row>
    <el-row justify="center">
      <div class="el-col el-col-24 el-col-xs-24 el-col-sm-20 el-col-md-20 el-col-lg-16 el-col-xl-12" style="margin-top:20px; color: #4A4A4A;">
        The OpenFly platform's toolchain generates diverse collision-free trajectories with variable lengths and altitudes by  leveraging scene point clouds and semantic segmentation. 
      </div>
    </el-row>
    <el-row justify="center" style="margin-top: 20px;">
      <el-col :xs="24" :sm="20" :md="20" :lg="16" :xl="12" >
        <video controls preload playsinline style="width: 100%;">
          <source src="/video/traj.mp4" type="video/mp4">
        </video>
      </el-col>
    </el-row>

  </div>
</template>

<style scoped>

</style>