<template>
  <div>
    <div>
      <button @click="selectLatest" :class="{'clicked': latest}">최신순</button>
      <button @click="selectUpcoming" :class="{'clicked': upcoming}">상영예정순</button>
    </div>
    <div id='itemList' v-show="this.latest">
      <h3>최신 영화</h3>
      <div class="row mx-auto" >
        <div class='col-3 my-2' v-for="movie in latestMovies.slice(0,4*page)" :key="movie.id">
          <div class="card" style="width: 100%;" @click="goDetail(movie.id)" > 
            <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" class="card-img-top" style="width:100%; height: 25rem;" alt="#"> 
            <div class="card-body">
              <div>
                <h5 v-if="movie.title.length <= 14" style="font-size:100%; font-weight: bold;" class="card-title mb-0">{{ movie?.title }}</h5>
                <h5 v-if="movie.title.length > 14" style="font-size:100%; font-weight: bold;" class="card-title mb-0">{{ movie?.title.slice(0, 13)}}..</h5>
              </div>
              <p class="card-text mb-0" style="font-size:80%;">{{movie?.release_date}}</p>
              <div class="d-flex justify-content-between align-items-center px-2">
                <div>
                  <i class="fa-solid fa-star" style="color:#d63e1c"></i> <span class="card-text">{{movie?.vote_average}}</span>
                </div>
                <div>
                  <i class="fa-solid fa-heart" style="color:#d63e1c"></i> <span class="card-text">{{movie?.like_users.length}}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button @click="add" v-if="4*page < latestMovies?.length">더보기</button>
    </div>
    
    <div id='itemList' v-show="this.upcoming">
      <h3>상영예정 영화</h3>
      <div class="row mx-auto" >
        <div class='col-3 my-2' v-for="movie in upComingMovies.slice(0, 4*page)" :key="movie.id">
          <div class="card" style="width: 100%;" @click="goDetail(movie.id)" > 
            <img :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`" class="card-img-top" style="width:100%; height: 25rem;" alt="#"> 
            <div class="card-body">
              <div>
                <h5 v-if="movie.title.length <= 14" style="font-size:100%; font-weight: bold;" class="card-title mb-0">{{ movie?.title }}</h5>
                <h5 v-if="movie.title.length > 14" style="font-size:100%; font-weight: bold;" class="card-title mb-0">{{ movie?.title.slice(0, 13)}}..</h5>
              </div>
              <p class="card-text mb-0" style="font-size:80%;">{{movie?.release_date}}</p>
              <div class="d-flex justify-content-between align-items-center px-2">
                <div>
                  <i class="fa-solid fa-star" style="color:#d63e1c"></i> <span class="card-text">{{movie?.vote_average}}</span>
                </div>
                <div>
                  <i class="fa-solid fa-heart" style="color:#d63e1c"></i> <span class="card-text">{{movie?.like_users.length}}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button @click="add" v-if="4*page < upComingMovies?.length">더보기</button>
    </div>
  </div>
</template>

<script>


export default {
  name: 'LastestMovieView',
  data() {
    return {
      page:3,
      latest: true,
      upcoming: false,
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    },
    selectLatest(){
      this.latest = true,
      this.upcoming = false,
      this.page = 3
    },
    selectUpcoming(){
      this.latest = false,
      this.upcoming = true,
      this.page = 3
    },
    add(){
      this.page += 3
    } 
  },
  computed: {
    latestMovies() {
      return this.$store.getters.latestMovies
    },
    upComingMovies() {
      return this.$store.getters.upComingMovies
    }    
  },
  mounted() {
    window.scrollTo(0,0)
  },
}
</script>

<style scoped>
  #itemList {
    display: inline-block;
  }
  body {
    background: yellow;
    color: green;
  }
</style>

<style>

.button {
  border-radius: 30%;
  background-color: white;
}
.clicked {
  background-color: grey;
}
.card {
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.card img {
  object-fit: fill;
  transition:.3s;
}
.card img:hover {
	transform:scale(1.05);
}
</style>