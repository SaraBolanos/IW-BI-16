(function() {
  var Application, Utils,
    bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  window.DEMO = window.DEMO || {};

  Utils = {
    'transform': Modernizr.prefixed('transform').replace(/([A-Z])/g, (function(_this) {
      return function(str, m1) {
        return '-' + m1.toLowerCase();
      };
    })(this)).replace(/^ms-/, '-ms-'),
    'translate': (function(_this) {
      return function(x, y) {
        var tran, vals;
        tran = Modernizr.csstransforms3d ? 'translate3d' : 'translate';
        vals = Modernizr.csstransforms3d ? '(' + x + ', ' + y + ', 0)' : '(' + x + ', ' + y + ')';
        return tran + vals;
      };
    })(this)
  };

  Application = (function() {
    function Application() {
      this.update = bind(this.update, this);
      this.handleScroll = bind(this.handleScroll, this);
      DEMO.utils = Utils;
      this.$roller = $('.roller');
      this.$step = $('#steps li');
      this.$title = $('#titles li');
      this.min = 0;
      this.max = this.$step.length - 1;
      this.active_index = 0;
      this.$step.eq(this.active_index).addClass('active');
      this.$title.eq(this.active_index).addClass('active');
      this.observe();
    }

    Application.prototype.observe = function() {
      var _this = this;
      $(document).on('wheel', function(e) {
        if (!_this.maxIndexReached && e.originalEvent.deltaY > 0) {
          _this.next();
          e.preventDefault(); // Prevent default scroll behavior if not at max index
        }
        if (e.originalEvent.deltaY > 0) {
          _this.next();
        } else {
          _this.previous();
        }
      });
    };

    
    Application.prototype.previous = function() {
      if (this.active_index > this.min) {
        this.active_index--;
        this.update();
      }
    };

    Application.prototype.next = function() {
      if (this.active_index < this.max) {
        this.active_index++;
        this.update();
      }else {
        this.maxIndexReached = true; // Set flag to true when the last active index is reached
      }
    };

    Application.prototype.update = function() {
      var y = this.active_index ; // Adjust this calculation based on your requirements
      this.$roller.css(DEMO.utils.transform, DEMO.utils.translate(0, -y + "%")); // Updated y value calculation
      this.$step.removeClass('active');
      this.$title.removeClass('active');
      this.$step.eq(this.active_index).addClass('active');
      this.$title.eq(this.active_index).addClass('active');
    };

    return Application;

  })();

  $(function() {
    return DEMO.instance = new Application();
  });

}).call(this);
