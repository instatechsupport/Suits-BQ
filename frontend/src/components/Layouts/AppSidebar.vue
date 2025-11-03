<template>
  <div
    dir="rtl"
    class="sidebar card transition-all duration-300 ease-in-out"
    :class="isSidebarCollapsed ? 'collapsed' : 'expanded'"
  >
    <!-- User Profile -->
    <div class="profile">
      <UserDropdown :isCollapsed="isSidebarCollapsed" />
    </div>

    <!-- Navigation -->
    <nav v-if="!isSidebarCollapsed" class="nav">
      <div
        v-for="view in allViews"
        :key="view.label"
        class="nav-section"
      >
        <div
          v-if="!view.hideLabel"
          class="section-label"
        >
          {{ __(view.name) }}
        </div>

        <div
          v-for="link in view.views"
          :key="link.label"
          class="nav-item"
          @click="$router.push(link.to)"
        >
          <div class="icon-wrap">
            <component :is="link.icon" class="nav-icon" />
          </div>
          <span class="nav-text">{{ __(link.label) }}</span>
        </div>
      </div>
    </nav>

    <!-- Collapsed Mode -->
    <nav v-else class="nav-collapsed">
      <div
        v-for="view in allViews"
        :key="view.label"
        class="nav-collapsed-group"
      >
        <div
          v-for="link in view.views"
          :key="link.label"
          class="nav-icon-only"
          @click="$router.push(link.to)"
        >
          <div class="icon-wrap">
            <component :is="link.icon" class="nav-icon" />
          </div>
        </div>
      </div>
    </nav>

    <!-- Collapse Button -->
    <div class="sidebar-footer">
      <button
        class="toggle-btn"
        @click="isSidebarCollapsed = !isSidebarCollapsed"
      >
        <CollapseSidebar
          class="toggle-icon"
          :class="{ rotated: isSidebarCollapsed }"
        />
        <span v-if="!isSidebarCollapsed">
          {{ isSidebarCollapsed ? __('Expand') : __('Collapse') }}
        </span>
      </button>
    </div>
  </div>
</template>

<style scoped>
/* ===== GLASS SIDEBAR ===== */
.sidebar {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  box-shadow: var(--shadow-1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  overflow: hidden;
  transition: all 0.3s ease-in-out;
}

.sidebar.expanded {
  width: 260px;
}
.sidebar.collapsed {
  width: 80px;
}

/* ===== PROFILE ===== */
.profile {
  padding: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: hsl(0 0% 100% / 0.35);
  border-bottom: 1px solid var(--glass-border);
}

/* ===== NAVIGATION ===== */
.nav {
  display: grid;
  gap: 12px;
  padding: 16px;
  overflow-y: auto;
}

.nav-section + .nav-section {
  margin-top: 1rem;
}

.section-label {
  font-size: 0.8rem;
  font-weight: 900;
  color: hsl(var(--h) 80% 75%);
  text-transform: uppercase;
  margin-bottom: 6px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 16px;
  cursor: pointer;
  border: 1px solid var(--glass-border);
  background: hsl(0 0% 100% / 0.3);
  transition: transform 0.15s ease, background 0.2s ease;
}
:root.dark .nav-item {
  background: hsl(0 0% 100% / 0.06);
}
.nav-item:hover {
  transform: translateY(-1px);
  background: linear-gradient(
    135deg,
    hsl(var(--h) 70% 60% / 0.25),
    hsl(var(--h) 70% 45% / 0.25)
  );
}

.icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  border: 1px solid var(--glass-border);
  background: linear-gradient(
    135deg,
    hsl(var(--h) 70% 60% / 0.25),
    hsl(var(--h) 70% 45% / 0.25)
  );
}

.nav-icon {
  width: 22px;
  height: 22px;
  color: hsl(var(--h) 80% 70%);
}

.nav-text {
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--txt);
}

/* ===== COLLAPSED ===== */
.nav-collapsed {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px 0;
  gap: 18px;
}
.nav-icon-only {
  cursor: pointer;
  transition: transform 0.2s ease;
}
.nav-icon-only:hover {
  transform: scale(1.1);
}

/* ===== FOOTER TOGGLE ===== */
.sidebar-footer {
  padding: 14px;
  display: flex;
  justify-content: center;
  border-top: 1px solid var(--glass-border);
}

.toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 0;
  background: transparent;
  color: hsl(var(--h) 80% 70%);
  font-weight: 800;
  cursor: pointer;
  transition: color 0.2s ease;
}
.toggle-btn:hover {
  color: hsl(var(--h) 85% 75%);
}

.toggle-icon {
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}
.toggle-icon.rotated {
  transform: rotateY(180deg);
}
</style>
