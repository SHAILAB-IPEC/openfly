<script>
import Title from './sections/Title.vue'
import Abstract from './sections/Abstract.vue'
import Markdown from './sections/Markdown.vue'
import BibTeX from './sections/BibTeX.vue'
import Carousel from './sections/Carousel.vue'
import Video from './sections/Video.vue'
import ImageSlider from './sections/ImageSlider.vue'
import ImageSliderInner from './sections/ImageSliderInner.vue'
import ImageSelector from './sections/ImageSelector.vue'
import Echart from './sections/Echart.vue'
import Table from './sections/Table.vue'
import Collapse from './sections/Collapse.vue'
import SeletionForComparison from './sections/SeletionForComparison.vue'
import Comment from './sections/Comment.vue'
import Latex from './sections/Latex.vue'
import Model3D from './sections/Model3D.vue'
import GaussianSplats3D from './sections/GaussianSplats3D.vue'
import Success from './sections/Success.vue'
import Path from './sections/Path.vue'
import Toolchain from './sections/Toolchain.vue'
import Model from './sections/Model.vue'
import Dataset from './sections/Dataset.vue'

export default {
  components: {
    Title,
    Abstract,
    Markdown,
    BibTeX,
    Carousel,
    Video,
    ImageSlider,
    ImageSliderInner,
    ImageSelector,
    Echart,
    Collapse,
    Table,
    SeletionForComparison,
    Comment,
    Latex,
    Model3D,
    GaussianSplats3D,
    Success,
    Path,
    Toolchain,
    Model,
    Dataset
  }
}
</script>

<template>
  <Title/>
  <Carousel/>
  
  <Abstract/>
  <Toolchain/>
  <Model/>
  <Video/>
  <ImageSliderInner/>
  <Path/>
  <!-- <ImageSlider/> -->
  <Dataset/>
  <Success/>
  <!-- <Markdown/> -->
  <!-- <Latex/> -->
  <!-- <Table/> -->
  <!-- <Collapse/> -->
  <!-- <Echart/> -->
  <!-- <Model3D/> -->
  <!-- <GaussianSplats3D/> -->
  <!-- <SeletionForComparison/> -->
  
  
  <!-- <ImageSelector/> -->
  <!-- <BibTeX/> -->
</template>