<template>
  <div>
    <div class='col-md-3 my-4' style='background-color:#D4964A'>
      <h3>계절 추천</h3>
    </div>
    <swiper
      class="swiper"
      :options="swiperOption"
    >
      <swiper-slide v-for="movie in weatherMovies" :key="movie.id" style="width: 100%;">
        <div class="card" style="width: 100%;" @click="goDetail(movie.id)" > 
          <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" class="card-img-top" style="width:100%; height:15rem;" alt="#"> 
          <div class="card-body">
            <div>
              <h5 v-if="movie.title.length <= 10" style="font-size:100%; font-weight: bold;" class="card-title mb-0">{{ movie.title }}</h5>
              <h5 v-if="movie.title.length > 10" style="font-size:100%; font-weight: bold;" class="card-title mb-0">{{ movie.title.slice(0, 8)}}..</h5>
            </div>
            <p class="card-text mb-0" style="font-size:80%;">{{movie.release_date}}</p>
            <div class="d-flex justify-content-between align-items-center px-2">
              <div>
                <i class="fa-solid fa-star" style="color:#d63e1c"></i> <span class="card-text">{{movie.vote_average}}</span>
              </div>
              <div>
                <i class="fa-solid fa-heart" style="color:#d63e1c"></i> <span class="card-text">{{movie.like_users.length}}</span>
              </div>
            </div>
            
          </div>
        </div>
      </swiper-slide>     
      <div
          class="swiper-pagination"
          slot="pagination"
          >
      </div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>


  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'WeatherList',
  data() {
    return {
      swiperOption: { 
        slidesPerView: 6, 
        spaceBetween: 20,
        slidesPerGroup: 6,
        loop: true, 
        loopFillGroupWithBlank: true,
        pagination: { 
          el: '.swiper-pagination', 
          clickable: true 
        }, 
        navigation: { 
          nextEl: '.swiper-button-next', 
          prevEl: '.swiper-button-prev' 
        } 
      },
    }
  },
  components: {
    Swiper,
    SwiperSlide
  },
  computed: {
    weatherMovies() {
      return this.$store.getters.weatherMovies
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    }
  },
}
</script>

<style scoped>
  h3 {
    color: white;
  }
  .card, h5, span{
    color: black;
  }
</style>
<style scoped>
.swiper {
  width: 100%;
  height: 80%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
  overflow: hidden;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-transform:scale(1);
	-moz-transform:scale(1);
	-ms-transform:scale(1);	
	-o-transform:scale(1);	
	transform:scale(1);
	-webkit-transition:.3s;
	-moz-transition:.3s;
	-ms-transition:.3s;
	-o-transition:.3s;
	transition:.3s;

}
.swiper-slide img:hover {
  -webkit-transform:scale(1.1);
	-moz-transform:scale(1.1);
	-ms-transform:scale(1.1);	
	-o-transform:scale(1.1);
	transform:scale(1.05);
}

.swiper-button-prev{
  color: white;
  -webkit-transform:scale(1);
	-moz-transform:scale(1);
	-ms-transform:scale(1);	
	-o-transform:scale(1);	
	transform:scale(1);
	-webkit-transition:.3s;
	-moz-transition:.3s;
	-ms-transition:.3s;
	-o-transition:.3s;
	transition:.3s;
}

.swiper-button-prev:hover{
  /* background-color: rgb(120, 120, 120, 0.5); */
  color: grey;
  -webkit-transform:scale(1.1);
	-moz-transform:scale(1.1);
	-ms-transform:scale(1.1);	
	-o-transform:scale(1.1);
  transform:scale(1.2);
}

.swiper-button-next{
  color: white;
  -webkit-transform:scale(1);
	-moz-transform:scale(1);
	-ms-transform:scale(1);	
	-o-transform:scale(1);	
	transform:scale(1);
	-webkit-transition:.3s;
	-moz-transition:.3s;
	-ms-transition:.3s;
	-o-transition:.3s;
	transition:.3s;
}

.swiper-button-next:hover{
  /* background-color: rgb(120, 120, 120, 0.5);
  border-radius: 10%; */
  color: grey;
  -webkit-transform:scale(1.1);
	-moz-transform:scale(1.1);
	-ms-transform:scale(1.1);	
	-o-transform:scale(1.1);
  transform:scale(1.2);
}

.swiper-pagination {
  
  position: relative;
  top: 5px;
}
.swiper-pagination-bullet {
  background-color: white;
}
</style>