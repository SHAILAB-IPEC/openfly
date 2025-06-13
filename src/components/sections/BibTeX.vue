<script>
export default {
  data() {
    return {
      bibtex: [
`@article{OpenFly,
  author       = {Yunpeng Gao and
                  Chenhui Li and
                  Zhongrui You and
                  Junli Liu and
                  Zhen Li and
                  Pengan Chen and
                  Qizhi Chen and
                  Zhonghan Tang and
                  Liansheng Wang and
                  Penghui Yang and
                  Yiwen Tang and
                  Yuhang Tang and
                  Shuai Liang and
                  Songyi Zhu and
                  Ziqin Xiong and
                  Yifei Su and
                  Xinyi Ye and
                  Jianan Li and
                  Yan Ding and
                  Dong Wang and
                  Zhigang Wang and
                  Bin Zhao and
                  Xuelong Li},
  title        = {OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation},
  journal      = {CoRR},
  volume       = {abs/2502.18041},
  year         = {2025}
}`
      ],
    }
  },
  methods: {
    copyVal() {
      let oInput = document.createElement('textarea');
      let text = document.getElementById('bibtex').innerText;
      oInput.value = text;
      document.body.appendChild(oInput);
      oInput.select();
      document.execCommand('Copy');
      this.$message.success('Copy Successfully');
      oInput.remove();
    }
  }
}

</script>

<template>
  <div>
    <el-divider />
      
      <el-row justify="center">
        <h1 class="section-title">BibTeX</h1>
      </el-row>
      
      <el-row justify="center">
        <el-col class='bibtex' :xs="24" :sm="20" :md="14" :lg="12" :xl="12" @click="copyVal()" >
          <div style="text-align: center; color: var(--el-text-color-secondary); margin-top: 20px;">🖱️ Click here to copy BibTex.</div> 
          <el-row>
              <el-scrollbar style="margin: 0px 20px 5px 20px;">
                <pre id="bibtex"><code v-for="b in bibtex">{{ b }}<br/></code></pre>
              </el-scrollbar>
          </el-row>
        </el-col>
      </el-row>

  </div>
</template>

<style scoped>

.scrollbar-flex-content {
  display: flex;
}

/* 卡片属性 */
.bibtex {
  margin: 20px 0px;
  padding-top: 5px;
  box-shadow: var(--el-box-shadow-light); 
  border-radius: 10px;
}

/* 卡片悬浮 */
.bibtex:hover {
  box-shadow: var(--el-box-shadow); 
}

/* 卡片点击 */
.bibtex:active{
  box-shadow: var(--el-box-shadow-lighter); 
}

pre {
  border: none;
  border-radius: 0px;
  padding: 10px;
  background: none;
}

pre code {
  font-size: 18px;
  background: #ffffff;
}



</style>